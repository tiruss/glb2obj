import os
import trimesh
import argparse

def extract_glb(glb_path):

    base_output_dir = os.path.basename(glb_path).split(".")[0]
    # 출력 디렉토리 생성
    output_dir = os.path.join("output", base_output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # Mesh 데이터 추출 및 저장
    scene = trimesh.load(glb_path)
    print(output_dir)
    obj_path = os.path.join(output_dir, "model.obj")
    scene.export(obj_path)
    print(f"Saved OBJ: {obj_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--glb_file", help="GLB file path")
    args = parser.parse_args()
    extract_glb(args.glb_file)

