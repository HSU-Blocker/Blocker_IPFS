import ipfshttpclient
import hashlib
import os

def upload_file(file_path):
    """
    주어진 파일을 IPFS에 업로드하고, 파일의 CID와 SHA-3 해시값을 반환하는 함수입니다.
    """
    try:
        # IPFS 노드에 연결 (기본 주소: localhost:5001)
        client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
        
        # 파일 존재 여부 확인
        if not os.path.isfile(file_path):
            print(f"⚠️ 파일이 존재하지 않습니다: {file_path}")
            return None, None

        # 파일을 바이너리 모드로 읽기
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # IPFS에 파일 업로드 (add_bytes 메서드 사용)
        cid = client.add_bytes(file_data)
        print("✅ 파일 업로드 성공! CID:", cid)
        
        # SHA-3 해시 계산 (SHA3-256 사용)
        sha3_hash = hashlib.sha3_256(file_data).hexdigest()
        print("🔑 SHA-3 해시:", sha3_hash)
        
        return cid, sha3_hash

    except Exception as e:
        print("🚨 파일 업로드 중 오류 발생:", e)
        return None, None

if __name__ == '__main__':
    # 🔹 정확한 경로 설정
    project_dir = "C:/Users/a/OneDrive/Desktop/IPFS/Blocker_IPFS/"
    file_path = os.path.join(project_dir, "encrypted_file.bin")  # AES 암호화된 파일

    # 🔹 IPFS에 업로드 실행
    cid, file_hash = upload_file(file_path)

    if cid:
        print("\n✅ IPFS 업로드 완료")
        print(f"🌐 CID: {cid}")
        print(f"🔗 파일 경로: {file_path}")
