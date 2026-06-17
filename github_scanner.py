import requests


def github_panel_ara(keyword):
    print(f"[*] GitHub uzerinde '{keyword}' kelimesi araniyor...")

    # GitHub API arama adresi
    url = f"https://api.github.com/search/repositories?q={keyword}+in:name,description,readme"

    try:
        # İsteği gönderiyoruz
        response = requests.get(url)

        if response.status_code == 200:
            veri = response.json()
            toplam_sonuc = veri.get("total_count", 0)
            print(f"[+] Toplam {toplam_sonuc} potansiyel depo bulundu.\n")

            # Bulunan ilk 5 depoyu ekrana yazdıralım
            depolar = veri.get("items", [])[:5]
            for repo in depolar:
                print("-" * 50)
                print(f"Depo Adi: {repo['full_name']}")
                print(f"Baglanti: {repo['html_url']}")
                print(f"Aciklama: {repo['description']}")
        else:
            print(f"[-] Hata olustu! GitHub API kodu: {response.status_code}")
    except Exception as e:
        print(f"[-] Baglanti hatasi: {e}")


if __name__ == "__main__":
    # Aramak istediğin kelimeyi buraya yazabilirsin
    github_panel_ara("sorgu paneli")
