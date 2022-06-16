import cv2
from barcode_service import BarcodeService

def test_success_upload_read_frame():

    service = BarcodeService()

    # given
    cases = {
        "case 1" : [True, True, True],
        "case 2" : [True, True, False],
        "case 3" : [True, False, True],
        "case 4" : [False, True, True],
        "case 5" : [True, False, False],
        "case 6" : [False, True, False],
        "case 7" : [False, False, True],
        "case 8" : [False, False, False],
    }
    
    targets = []
    result_list = dict()

    for i in range(1,24):
        targets.append("barcode_" + str(i) + ".jpeg")

    # when
    for k, case in cases.items():
        value_results = []
        index_results = []
        for target in targets:

            img = cv2.imread('sample_udi/' + target)

            preprocessed_img = service.preprocessing(img=img, gray=case[0], sharpen= case[1], threshold= case[2])

            result = service._read_frame(preprocessed_img)

            value_results.append(result.get("msg"))

    
        for index, result in enumerate(value_results):
            if result:
                index_results.append(index)

        point = len(index_results) / len(targets)

        result_list[k] = point
    
    result_list = sorted(result_list.items(), key=lambda x : x[1], reverse=True)
    
    for result in result_list:
        case = cases[result[0]]
        print()
        print(f"{result[0]} gray = {case[0]}, shrpen = {case[1]}, threshold = {case[2]}")
        print(f"==> {result[1]}")
        print()

if __name__ == "__main__":
    test_success_upload_read_frame()