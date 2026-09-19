from PIL import Image
import os

# =====================================================================
# 설정: resize 대상 폴더 목록 및 장변 최대 크기
# =====================================================================
folders    = ["train1", "train2", "test1", "test2"]  # resize 대상 폴더
max_size   = 400                                      # 장변 최대 픽셀 수

# =====================================================================
# 메인 처리
# =====================================================================
for folder in folders:
    if not os.path.isdir(folder):
        print(f"[건너뜀] 폴더 없음: {folder}")
        continue

    jpg_files = [f for f in os.listdir(folder) if f.lower().endswith(".jpg")]

    if not jpg_files:
        print(f"[건너뜀] jpg 파일 없음: {folder}")
        continue

    print(f"\n[처리 중] {folder}/ ({len(jpg_files)}개 파일)")

    for filename in jpg_files:
        filepath = os.path.join(folder, filename)

        img = Image.open(filepath).convert("RGB")
        w, h = img.size

        # 장변이 이미 max_size 이하이면 skip
        if max(w, h) <= max_size:
            print(f"  [skip] {filename}  ({w}x{h})")
            continue

        # 비율 유지하며 장변 기준으로 resize
        if w >= h:
            new_w = max_size
            new_h = int(h * max_size / w)
        else:
            new_h = max_size
            new_w = int(w * max_size / h)

        img_resized = img.resize((new_w, new_h), Image.LANCZOS)
        img_resized.save(filepath, "JPEG", quality=90)

        print(f"  [완료] {filename}  ({w}x{h}) -> ({new_w}x{new_h})")

print("\n모든 처리가 완료되었습니다.")