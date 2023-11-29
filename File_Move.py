import shutil
import os
import zipfile

def move_and_overwrite(source_path, destination_path):
    try:
        # 파일을 이동하고 덮어쓰기
        shutil.move(source_path, destination_path)
        print(f'파일을 {destination_path}로 성공적으로 이동하였습니다.')
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {source_path}')
    except PermissionError:
        print(f'권한이 없어 파일을 이동할 수 없습니다: {source_path}')
    except Exception as e:
        print(f'오류 발생: {e}')

def extract_zip(zip_file_path, extract_to_path):
    try:
        # 압축 파일 열기
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # 압축 해제
            zip_ref.extractall(extract_to_path)
            print(f'{zip_file_path}를 {extract_to_path}에 성공적으로 압축 해제하였습니다.')
    except zipfile.BadZipFile:
        print(f'{zip_file_path}는 유효한 압축 파일이 아닙니다.')
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {zip_file_path}')
    except PermissionError:
        print(f'권한이 없어 파일을 압축 해제할 수 없습니다: {zip_file_path}')
    except Exception as e:
        print(f'오류 발생: {e}')
source_file = './lotSetup.xml'
destination_file = 'C:/temp/TPAD_Tool_2.3.17/lotSetup.xml'

zip_file_path = './LP 개선 TPAD.zip'
extract_to_path = 'C:/IT'

move_and_overwrite(source_file, destination_file)
extract_zip(zip_file_path, extract_to_path)

