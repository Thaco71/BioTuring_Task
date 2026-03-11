import re
import urllib.request
import urllib.error
import time

def clean_uniprot_id(uniprot_id):
    """Lấy phần ID chính (trước dấu gạch dưới đầu tiên)"""
    return uniprot_id.split('_')[0]

def get_protein_sequence(uniprot_id):
    """Lấy chuỗi protein từ UniProt dựa trên ID"""
    clean_id = clean_uniprot_id(uniprot_id)
    url = f"http://www.uniprot.org/uniprot/{clean_id}.fasta"
    
    # Thêm User-Agent header để tránh bị chặn
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            # Bỏ qua dòng đầu tiên (header) và nối các dòng còn lại
            lines = data.strip().split('\n')
            sequence = ''.join(lines[1:])
            return sequence
    except urllib.error.HTTPError as e:
        print(f"Lỗi HTTP khi truy cập {uniprot_id} ({clean_id}): {e}")
        return None
    except urllib.error.URLError as e:
        print(f"Lỗi URL khi truy cập {uniprot_id} ({clean_id}): {e}")
        return None
    except Exception as e:
        print(f"Lỗi không xác định khi truy cập {uniprot_id} ({clean_id}): {e}")
        return None

def find_nglycosylation_motif(sequence):
    """Tìm vị trí của motif N-glycosylation trong chuỗi protein"""
    positions = []
    
    for i in range(len(sequence) - 3):
        if (sequence[i] == 'N' and 
            sequence[i+1] != 'P' and 
            sequence[i+2] in ['S', 'T'] and 
            sequence[i+3] != 'P'):
            positions.append(i + 1)
    
    return positions

def main():
    # Đọc file input
    with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_mprt.txt', 'r') as f:
        uniprot_ids = [line.strip() for line in f if line.strip()]
    
    print(f"Đọc được {len(uniprot_ids)} ID từ file")
    
    # Xử lý từng ID
    for i, uniprot_id in enumerate(uniprot_ids, 1):
        print(f"\nĐang xử lý ID {i}/{len(uniprot_ids)}: {uniprot_id}")
        
        sequence = get_protein_sequence(uniprot_id)
        
        if sequence:
            print(f"  Đã lấy được sequence, độ dài: {len(sequence)}")
            positions = find_nglycosylation_motif(sequence)
            
            if positions:
                print(f"  Tìm thấy {len(positions)} vị trí motif")
                print(uniprot_id)
                print('_'.join(map(str, positions)))
            else:
                print(f"  Không tìm thấy motif")
        
        # Tạm dừng một chút để tránh quá tải server
        time.sleep(0.5)

if __name__ == "__main__":
    main()