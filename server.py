cat << 'EOF' > server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

ziyaretciler = []
banli_ipleri = []
ip_to_name = {}
kullanici_sayaci = 1

# Siber Güvenlik & Oyun Hileleri Veritabanı Simülasyonu
hile_veritabani = {
    "gta": [
            {"baslik": "GTA V Online - %100 Safe Mod Menu v4.2", "link": "https://github.com/SiberGuvenlik/gta5-modmenu"},
                    {"baslik": "GTA San Andreas - Tüm Gizli Hile Kodları Arşivi (PC/Konsol)", "link": "https://github.com/SiberGuvenlik/gtasa-cheats"}
                        ],
                            "valorant": [
                                    {"baslik": "Valorant - Esp & Aimbot Bypass Driver v2.1", "link": "https://github.com/SiberGuvenlik/val-bypass"},
                                            {"baslik": "Valorant - Skin Changer Hack (Anti-Cheat Safe)", "link": "https://github.com/SiberGuvenlik/val-skinchanger"}
                                                ],
                                                    "cs": [
                                                            {"baslik": "Counter-Strike 2 - Wallhack & Skin Changer Source Code", "link": "https://github.com/SiberGuvenlik/cs2-wallhack"},
                                                                    {"baslik": "CS:GO - Legit Aimbot Config & Injector v9.0", "link": "https://github.com/SiberGuvenlik/csgo-legit"}
                                                                        ],
                                                                            "pubg": [
                                                                                    {"baslik": "PUBG Mobile - No Recoil & Antiban Config (Sezon 2026)", "link": "https://github.com/SiberGuvenlik/pubgm-norecoil"},
                                                                                            {"baslik": "PUBG Steam - Radar Hack & ESP Script v3.1", "link": "https://github.com/SiberGuvenlik/pubg-radar"}
                                                                                                ],
                                                                                                    "brawl": [
                                                                                                            {"baslik": "Brawl Stars - Sınırsız Taş & Altın Hileli Mod (Nulls Brawl)", "link": "https://github.com/SiberGuvenlik/brawl-stars-mod"}
                                                                                                                ],
                                                                                                                    "lol": [
                                                                                                                            {"baslik": "League of Legends - Evade & Orbwalker Script v16.2", "link": "https://github.com/SiberGuvenlik/lol-script"}
                                                                                                                                ]
                                                                                                                                }

                                                                                                                                @app.route('/')
                                                                                                                                def home(): return "Siber Güvenlik Ana Merkez Sunucusu Aktif!"

                                                                                                                                @app.route('/api/ziyaret-kaydet', methods=['POST'])
                                                                                                                                def ziyaret_kaydet():
                                                                                                                                    global kullanici_sayaci
                                                                                                                                        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
                                                                                                                                            if ip in banli_ipleri: return jsonify({"durum": "engellendi", "mesaj": "Siber Güvenlik Paneli tarafından engellendiniz!"}), 403
                                                                                                                                                if ip not in ip_to_name:
                                                                                                                                                        ip_to_name[ip] = f"User {kullanici_sayaci}"
                                                                                                                                                                kullanici_sayaci += 1
                                                                                                                                                                    ziyaretciler.append({"ad": ip_to_name[ip], "ip": ip, "cihaz": request.headers.get('User-Agent', 'Bilinmiyor')[:30], "saat": datetime.now().strftime('%H:%M:%S')})
                                                                                                                                                                        return jsonify({"durum": "basarili", "mesaj": "Ziyaret kaydedildi."})

                                                                                                                                                                        @app.route('/api/ara', methods=['GET'])
                                                                                                                                                                        def siber_ara():
                                                                                                                                                                            kelime = request.args.get('q', '').lower()
                                                                                                                                                                                sonuclar = []
                                                                                                                                                                                    
                                                                                                                                                                                        # Hile kelime eşleştirmesi
                                                                                                                                                                                            for anahtar, hileler in hile_veritabani.items():
                                                                                                                                                                                                    if anahtar in kelime:
                                                                                                                                                                                                                sonuclar.extend(hileler)
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                # Genel Siber Güvenlik sonuçları (Eğer hile bulunamazsa veya ekstra olarak)
                                                                                                                                                                                                                                    if not sonuclar or "sorgu" in kelime or "siber" in kelime:
                                                                                                                                                                                                                                            sonuclar.append({"baslik": f"Siber Güvenlik Veritabanı: '{kelime}' Analiz Raporu.pdf", "link": "https://github.com/SiberGuvenlik/analiz"})
                                                                                                                                                                                                                                                    sonuclar.append({"baslik": "İllegal Siber Panel Tarayıcı & Exploiter Bot v1.0", "link": "https://github.com/SiberGuvenlik/exploiter"})
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                return jsonify({"toplam": len(sonuclar), "sonuclar": sonuclar})

                                                                                                                                                                                                                                                                @app.route('/api/ziyaretciler', methods=['GET'])
                                                                                                                                                                                                                                                                def ziyaretcileri_getir(): return jsonify(ziyaretciler)

                                                                                                                                                                                                                                                                @app.route('/api/banla', methods=['POST'])
                                                                                                                                                                                                                                                                def ip_banla():
                                                                                                                                                                                                                                                                    hedef_ad = request.json.get("ad", "")
                                                                                                                                                                                                                                                                        hedef_ip = next((ip for ip, ad in ip_to_name.items() if ad.lower() == hedef_ad.lower()), None)
                                                                                                                                                                                                                                                                            if hedef_ip:
                                                                                                                                                                                                                                                                                    if hedef_ip not in banli_ipleri:
                                                                                                                                                                                                                                                                                                banli_ipleri.append(hedef_ip)
                                                                                                                                                                                                                                                                                                            return jsonify({"durum": "basarili", "mesaj": f"{hedef_ad} başarıyla banlandı!"})
                                                                                                                                                                                                                                                                                                                    return jsonify({"durum": "bilgi", "mesaj": f"{hedef_ad} zaten banlı."})
                                                                                                                                                                                                                                                                                                                        return jsonify({"durum": "hata", "mesaj": f"'{hedef_ad}' bulunamadı."})

                                                                                                                                                                                                                                                                                                                        if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
                                                                                                                                                                                                                                                                                                                        EOF
                                                                                                                                                                                                                                                                                                                        