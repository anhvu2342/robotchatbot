import json
from datetime import datetime


class ChatProcess():
    def findcontact(self, info, index):
        contacts = self._read_contacts()
        for contact in contacts:
            if index == 1 and contact[0] == info:       # Tìm theo username
                return contact[0], contact[1], contact[2]
            elif index == 2 and contact[1] == info:     # Tìm theo name
                return contact[0], contact[1], contact[2]
            elif index == 3 and contact[2] == info:     # Tìm theo email
                return contact[0], contact[1], contact[2]
        return None, None, None                         # Nếu không tìm thấy

    def _read_contacts(self):
        contacts = []
        with open("contact.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                contacts.append(line.strip().split(','))
        return contacts
    def createnewchat(self,filename, ten_cuoc_tro_chuyen):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        cuoc_tro_chuyen_moi = {
            "cuoc_tro_chuyen": ten_cuoc_tro_chuyen,
            "lich_su": []
        }
        data.append(cuoc_tro_chuyen_moi)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Cuộc trò chuyện mới đã được thêm vào.")
    def showhistory(self, filename, ten_cuoc_tro_chuyen):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for cuoc_tro_chuyen in data:
            if cuoc_tro_chuyen["cuoc_tro_chuyen"] == ten_cuoc_tro_chuyen:
                txt = ""
                for message in cuoc_tro_chuyen.get("lich_su", cuoc_tro_chuyen.get("noi_dung", [])):
                    txt = txt + f'{message["nguoi_gui"]}: {message["noi_dung"]}\n'
                    #print(f'{message["nguoi_gui"]}: {message["noi_dung"]}')
                return txt


    def storehistorychat(self, cuoctrochuyen, name, noidung):
        tin_nhan_moi = {
            "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nguoi_gui": name,
            "noi_dung": noidung
        }
        with open('chathistory.json', 'r', encoding='utf-8') as file:
            du_lieu = json.load(file)
        # Tìm cuộc trò chuyện
        found = False
        for cuoc_tro_chuyen in du_lieu:
            if cuoc_tro_chuyen["cuoc_tro_chuyen"] == cuoctrochuyen:
                # Thêm tin nhắn mới vào cuộc trò chuyện
                cuoc_tro_chuyen["lich_su"].append(tin_nhan_moi)
                found = True
                break                               # Thoát khỏi vòng lặp vì đã tìm thấy cuộc trò chuyện
        if not found:
            # Nếu không tìm thấy cuộc trò chuyện nào khớp, thêm cuộc trò chuyện mới
            cuoc_tro_chuyen_moi = {
                "cuoc_tro_chuyen": cuoctrochuyen,
                "lich_su": [tin_nhan_moi]
            }
            du_lieu.append(cuoc_tro_chuyen_moi)
        # Ghi lại nội dung đã cập nhật vào file JSON
        with open('chathistory.json', 'w', encoding='utf-8') as file:
            json.dump(du_lieu, file, ensure_ascii=False, indent=4)
