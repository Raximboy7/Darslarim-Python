class Isysteam:
    def __init__(self,oqtuvchilar,oquvchilar):
        self.oqtuvchilar = oqtuvchilar
        self.oquvchilar = oquvchilar

    def __str__(self,):
        return self.oqtuvchilar,self.oquvchilar

    def get_info(self):
        return f"O'qtuvchi ismi:{self.oqtuvchilar}\nO'quvchilar ismi:{self.oquvchilar}"
