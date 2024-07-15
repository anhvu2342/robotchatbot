import re
'''import math


# Hàm đọc số và thêm tên hàng đơn vị
def number_to_words_with_units(num):
    units = ["", "mười", "trăm", "nghìn", "mươi", "trăm", "triệu", "mươi", "trăm", "tỷ"]
    digits = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    # Tính số chữ số của num
    num_digits = math.ceil(math.log10(num + 1)) if num != 0 else 1
    num_str = str(num)
    result = []

    for i in range(num_digits):
        digit = int(num_str[i])
        unit = units[num_digits - i - 1]
        if unit == "mươi" and digit == 0:
            # Skip "mươi" if the digit is 0
            continue
        result.append(digits[digit])
        if unit:
            result.append(unit)

    return " ".join(result)


# Hàm thay thế số trong văn bản bằng chữ
def replace_numbers_with_words(text):
    def replace(match):
        number = int(match.group())
        words_with_units = number_to_words_with_units(number)
        return words_with_units

    # Sử dụng biểu thức chính quy để tìm tất cả các số và thay thế
    return re.sub(r'\b\d+\b', replace, text)


# Đoạn văn bản cần chuyển đổi
paragraph = "Bắc Ninh là một tỉnh nằm ở vùng Đồng bằng sông Hồng, nổi tiếng với nhiều món đặc sản ngon và độc đáo. Một số đặc sản nổi tiếng của Bắc Ninh bao gồm: \n1. Bánh đa nem Bắc Ninh: Bánh đa nem là một loại bánh truyền thống của vùng Bắc Bộ, nhưng ở Bắc Ninh có cách làm và hương vị riêng. Bánh được làm từ bột gạo, thịt nạc, mộc nhĩ, dầu mè và gia vị khác. Bánh đa nem Bắc Ninh thường được ăn kèm với nước mắm pha chua ngọt.\n2. Chả lụa Bắc Ninh: Chả lụa Bắc Ninh được chế biến từ thịt heo tươi ngon, được xay nhuyễn và trộn với gia vị truyền thống. Chả lụa Bắc Ninh thường được cuốn vào lá chuối và ăn kèm với bánh đa.\n3. Bún riêu cua Bắc Ninh: Một món ăn ngon và đặc trưng của Bắc Ninh là bún riêu cua, với nước dùng đậm đà, thơm ngon từ cua và các loại rau sống. Món ăn này thường được phục vụ nóng hổi, kèm theo bún, rau sống và một chút chanh.\nNgoài ra, Bắc Ninh cũng nổi tiếng với các loại mứt trái cây, rượu sim Bắc Ninh, bánh phu thê, bánh đa bắc Bộ và nhiều món ngon khác."

# Chuyển đổi số thành chữ và thêm số chữ số
converted_paragraph = replace_numbers_with_words(paragraph)
print(converted_paragraph)'''


# Các âm đầu tiếng Việt
initials = [
    'tr' ,'th', 'ph', 'ng', 'nh', 'kh', 'ch', 'gh', 'b', 'c', 'd', 'đ','h', 'g', 'k',  'l', 'm', 'n', 'q', 'r', 's', 't', 'v', 'x'
]

# Các âm chính tiếng Việt, không dùng
medials = [
    'a', 'ă', 'â', 'e', 'ê', 'i', 'o', 'ô', 'ơ', 'u', 'ư', 'y'
]

# Các âm cuối tiếng Việt
finals = [
    'ng', 'nh', 'c', 'ch', 'm', 'n', 'p', 't'
]


# Hàm bỏ dấu thanh điệu trong câu, giúp tối giản câu
def remove_diacritics(text):
    text = re.sub('[!,;?\n/]', '.', text)               # Loại bỏ các dấu câu, thay bằng dấu chấm
    text = text.lower()                                             # Loại bỏ chữ viết hoa, phục vụ việc xử lý sau này dễ hơn
    # Tạo bản đồ các ký tự có dấu sang ký tự không dấu
    diacritics_map = {
        'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ấ': 'â', 'ầ': 'â', 'ẩ': 'â', 'ẫ': 'â', 'ậ': 'â',
        'ắ': 'ă', 'ằ': 'ă', 'ẳ': 'ă', 'ẵ': 'ă', 'ặ': 'ă',
        'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ế': 'ê', 'ề': 'ê', 'ể': 'ê', 'ễ': 'ê', 'ệ': 'ê',
        'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ố': 'ô', 'ồ': 'ô', 'ổ': 'ô', 'ỗ': 'ô', 'ộ': 'ô',
        'ớ': 'ơ', 'ờ': 'ơ', 'ở': 'ơ', 'ỡ': 'ơ', 'ợ': 'ơ',
        'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ứ': 'ư', 'ừ': 'ư', 'ử': 'ư', 'ữ': 'ư', 'ự': 'ư',
        'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y'
    }

    # Dùng biểu thức chính quy để thay thế các ký tự có dấu
    pattern = re.compile("|".join(diacritics_map.keys()))
    return pattern.sub(lambda x: diacritics_map[x.group()], text)


# Hàm tách âm tiết thành các phần
def split_syllable(syllable):
    syllable = syllable.lower()
    initial = ''
    medial = ''
    final = ''

    # Tách âm đầu
    for init in initials:
        if syllable.startswith(init):
            initial = init
            syllable = syllable[len(init):]
            break

    # Tách âm cuối
    for fin in finals:
        if syllable.endswith(fin):
            final = fin
            syllable = syllable[:-len(fin)]
            break

    # Phần còn lại là âm chính
    medial = syllable

    return initial, medial, final

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


"""# Ví dụ sử dụng
words = ["xin", "chào", "bạn", "khỏe", "không", "nha", "khoản", "khuyển", "Khuya"]
for word in words:
    initial1, medial1, final1 = split_syllable(word)
    print(f"Từ: {word} - Âm đầu: {initial1}, Âm chính: {medial1}, Âm cuối: {final1}")
text = ("Thời tiết hôm nay đẹp! Tôi muốn đi chơi.")
print(remove_diacritics(text))
ascii_text = remove_diacritics(text)
print(ascii_text)"""