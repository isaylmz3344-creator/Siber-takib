from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# Farklı sitelerden (GitHub Pages gibi) bu sunucuya istek gelebilmesi için CORS'u açıyoruz
CORS(app)

# Ziyaretçilerin kaydedileceği liste (Sunucu açık kaldığı sürece hafızada durur)
ziyaretciler = []
# Banlanan IP'lerin listesi
banli_listesi = []

@app.route('/')
def home():
    return "Siber Takip Ana Sunucusu Aktif!"

    # Sitemiz açıldığında ziyaretçiyi kaydedecek olan endpoint
    @app.route('/api/ziyaret-kaydet', methods=['POST'])
    def ziyaret_kaydet():
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            user_agent = request.headers.get('User-Agent', 'Bilinmiyor')
                zaman = datetime.now().strftime('%H:%M:%S')
                    
                        # Eğer giren kişi banlıysa içeri alma
                            if ip in banli_listesi:
                                    return jsonify({"durum": "engellendi", "mesaj": "Bu IP sistemden banlanmıştır!"}), 403
                                            
                                                yeni_ziyaretci = {
                                                        "ip": ip,
                                                                "cihaz": user_agent[:50], # Cihaz bilgisinin sadece ilk 50 karakteri
                                                                        "saat": zaman
                                                                            }
                                                                                
                                                                                    # Listeye ekle (Aynı IP üst üste girmesin diye istersen kontrol koyabilirsin ama şimdilik her girişi bassın)
                                                                                        ziyaretciler.append(yeni_ziyaretci)
                                                                                            return jsonify({"durum": "basarili", "mesaj": "Ziyaret kaydedildi."})

                                                                                            # Admin panelinin ziyaretçileri çekeceği endpoint
                                                                                            @app.route('/api/ziyaretciler', methods=['GET'])
                                                                                            def ziyaretcileri_getir():
                                                                                                return jsonify(ziyaretciler)

                                                                                                # Admin panelinden birini banlamak için kullanılacak endpoint
                                                                                                @app.route('/api/banla', methods=['POST'])
                                                                                                def ip_banla():
                                                                                                    data = request.json
                                                                                                        banlanacak_ip = data.get("ip")
                                                                                                            if banlanacak_ip and banlanacak_ip not in banli_listesi:
                                                                                                                    banli_listesi.append(banlanacak_ip)
                                                                                                                            return jsonify({"durum": "basarili", "mesaj": f"{banlanacak_ip} başarıyla banlandı."})
                                                                                                                                return jsonify({"durum": "hata", "mesaj": "Geçersiz IP."})

                                                                                                                                if __name__ == '__main__':
                                                                                                                                    # Sunucuyu yerelde test etmek veya buluta açmak için hazır hale getiriyoruz
                                                                                                                                        app.run(host='0.0.0.0', port=5000)
                                                                                                                                        