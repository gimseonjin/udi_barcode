"""
This is Barcode Service Test!!

For find best case, test various cases
"""
import cv2
from barcode_server.service.barcode_service import BarcodeService

def test_success_upload_read_frame():
    """
    Title : test_success_upload_read_frame

    Find Best Case!!!

    Test Case - case Num - "gray scale", "sharpening", "threshold"
        "case 1" : [True, True, True],
        "case 2" : [True, True, False],
        "case 3" : [True, False, True],
        "case 4" : [False, True, True],
        "case 5" : [True, False, False],
        "case 6" : [False, True, False],
        "case 7" : [False, False, True],
        "case 8" : [False, False, False],
    """

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
    for i in range(1,25):
        targets.append("barcode_" + str(i) + ".jpeg")

    # when
    result_list = {}
    for k, case in cases.items():
        success_case = 0

        for target in targets:

            img = cv2.imread('sample_udi/' + target)

            preprocessed_img = service.preprocessing(img=img, gray=case[0], sharpen= case[1], threshold= case[2])

            result = service.read_frame(preprocessed_img)

            if result.get("msg") :
                success_case += 1

        rate = success_case / len(targets)

        result_list[k] = rate

    result_list = sorted(result_list.items(), key=lambda x : x[1], reverse=True)

    # then
    for result in result_list:
        case = cases[result[0]]
        print()
        print(f"{result[0]} gray = {case[0]}, shrpen = {case[1]}, threshold = {case[2]}")
        print(f"==> {result[1]}")
        print()

if __name__ == "__main__":
    test_success_upload_read_frame()
