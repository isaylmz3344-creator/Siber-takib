import requests
import json
import time

# Terminali renklendirmek için kullanılan kodlar
YEŞİL = "\033[92m"
KIRMIZI = "\033[91m"
SARI = "\033[93m"
MAVİ = "\033[94m"
BEYAZ = "\033[0m"
BOLD = "\033[1m"

print(YEŞİL + BOLD + """
==================================================
        SİBER TAKİP - İLLEGAL PANEL AVCISI v2.5       
        ==================================================
        [+] Sistem Başlatıldı...
        [+] Tarama Modülü: GitHub API v3
        ==================================================""" + BEYAZ)

        def siber_tarama():
            aranacak_kelime = input(SARI + "\n[?] Taramak istediğiniz siber tehdit kelimesini yazın (Örn: sorgu paneli): " + BEYAZ)
                
                    if not aranacak_kelime:
                            aranacak_kelime = "sorgu paneli"
                                    
                                        print(MAVİ + f"\n[*] GitHub üzerinde '{aranacak_kelime}' kelimesi aranıyor..." + BEYAZ)
                                            time.sleep(1) 
                                                
                                                    url = f"https://api.github.com/search/repositories?q={aranacak_kelime}+in:name,description,readme"
                                                        
                                                            try:
                                                                    response = requests.get(url)
                                                                            
                                                                                    if response.status_code == 200:
                                                                                                veri = response.json()
                                                                                                            toplam_sonuc = veri.get('total_count', 0)
                                                                                                                        
                                                                                                                                    print(YEŞİL + f"[+] Tarama Tamamlandı! Toplam {toplam_sonuc} potansiyel riskli depo bulundu.\n" + BEYAZ)
                                                                                                                                                print(YEŞİL + "================= SİBER ANALİZ RAPORU =================" + BEYAZ)
                                                                                                                                                            
                                                                                                                                                                        for sira, depo in enumerate(veri.get('items', [])[:5], 1):
                                                                                                                                                                                        print(MAVİ + f"\n[{sira}] Depo Adı: " + BEYAZ + BOLD + depo['full_name'] + BEYAZ)
                                                                                                                                                                                                        print(SARI + f" └── Açıklama: " + BEYAZ + (depo['description'] if depo['description'] else "Açıklama bırakılmamış."))
                                                                                                                                                                                                                        print(SARI + f" └── Bağlantı Linki: " + BEYAZ + depo['html_url'])
                                                                                                                                                                                                                                        print(SARI + f" └── Yıldız Sayısı: " + BEYAZ + str(depo['stargazers_count']))
                                                                                                                                                                                                                                                        print("-" * 50)
                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                    print(YEŞİL + "\n[+] Raporlama bitti. Şüpheli depolar USOM'a bildirilebilir." + BEYAZ)
                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                    print(KIRMIZI + f"[-] Bağlantı Hatası! GitHub API hata kodu döndürdü: {response.status_code}" + BEYAZ)
                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                                                                                                                            print(KIRMIZI + f"[-] Kritik Sistem Hatası: {e}" + BEYAZ)

                                                                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                siber_tarama()
                                                                                                                                                                                                                                                                                                                                                