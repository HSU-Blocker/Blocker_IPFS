import ipfshttpclient
import hashlib
import os

def download_file(cid, output_path, expected_hash=None):
    """
    IPFS에 저장된 파일을 CID를 통해 다운로드하여 지정된 경로에 저장하고,
    다운로드한 파일의 SHA-3 해시를 계산한 후 무결성을 검증하는 함수입니다.
    """
    try:
        # IPFS 노드에 연결
        client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

        # CID에 해당하는 파일 다운로드
        print(f"📥 CID {cid} 에서 파일 다운로드 중...")
        file_data = client.cat(cid)

        # 파일 데이터를 지정된 경로에 저장
        with open(output_path, 'wb') as f:
            f.write(file_data)
        print(f"✅ 파일 다운로드 완료: {output_path}")

        # 다운로드한 파일의 SHA-3 해시 계산
        sha3_hash = hashlib.sha3_256(file_data).hexdigest()
        print(f"🔑 다운로드된 파일 SHA-3 해시: {sha3_hash}")

        # 무결성 검사 (업로드된 해시와 비교)
        if expected_hash:
            if sha3_hash == expected_hash:
                print("✅ 데이터 무결성 확인 완료 (해시 일치) 🔒")
            else:
                print("⚠️ 데이터 무결성 검증 실패 (해시 불일치) ❌")

        return sha3_hash

    except Exception as e:
        print(f"🚨 파일 다운로드 중 오류 발생: {e}")
        return None

if __name__ == '__main__':
    # 📌 사용자 입력
    cid = input("📌 다운로드할 파일의 CID를 입력하세요: ").strip()

    # 📂 프로젝트 디렉토리 경로 설정
    project_dir = "C:/Users/a/OneDrive/Desktop/IPFS/Blocker_IPFS/"
    output_path = os.path.join(project_dir, "downloaded_update.bin")  # 저장 경로

    # 🔹 업로드 시 저장된 SHA-3 해시값 (옵션)
    expected_hash = input("📌 원본 파일의 SHA-3 해시값을 입력하세요 (무결성 검증용, 없으면 Enter): ").strip() or None

    # 🔽 다운로드 실행
    downloaded_hash = download_file(cid, output_path, expected_hash)
