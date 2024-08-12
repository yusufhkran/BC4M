## Projeyi Hazırlama Adımlarım

### Görevler

1. **API Bilgilerini Geliştirme**
   - API nedir? Ne işe yarar? Nasıl yazılır? gibi sorulara cevap aradım.
   - Daha önce API yazmadığım için, API hakkında bilgi edinmeye ve uygun yazılım dilini seçmeye karar verdim.

2. **Yazılım Dili Seçimi**
   - API yazmak ilk bakışta zor bir görev gibi görünüyordu. Bu yüzden, daha önceden tanışık olduğum ve giriş seviyede bilgi sahibi olduğum Golang dilini seçtim.
   - Ancak, Golang bilgim yetersiz kaldı ve bu süreçte zaman kaybetmek istemedim. Python dilini tercih ederek API'yi Python ile yazmaya karar verdim.

3. **İlk Görev: Python ile API Geliştirme**
   - Python ve Flask kullanarak API'yi geliştirdim.
   - Postman aracılığıyla gönderdiğim isteklerle ilk görevi tamamladım.

4. **Docker Dosyası Yazımı**
   - Docker bilgim sayesinde Docker dosyasını yazmakta zorlanmadım.
   - Docker dosyasının adımları:
     - `FROM` ile Python ve Linux Alpine tabanlı bir imaj seçtim.
     - `WORKDIR` ile proje dosyalarını kopyaladım.
     - `RUN pip install -r requirements.txt` ile bağımlılıkları yükledim.
     - `EXPOSE 5000` ile portu açtım.
     - `CMD` ile uygulama komutunu verdim.

5. **Docker İmajı Oluşturma ve Container Başlatma**
   - `docker build -t yusufhkran/bc4m_apiimage:0.1 .` komutuyla imajı oluşturdum.
   - `docker container run -d --name bc4m_apideneme1 yusufhkran/bc4m_apiimage:0.1` komutuyla container başlattım.
   - 127.0.0.1:5000 adresine bağlanırken sorun yaşadım. Sorunun, uygulamanın dış dünyaya kapalı olması nedeniyle olduğunu fark ettim.
   - `app.run(debug=True, host="0.0.0.0", port=5000)` ayarını yaparak uygulamanın dış dünyaya açılmasını sağladım.

6. **Port Yayını**
   - Docker container'ını `docker container run -d -p 5000:5000 --name bc4m_apideneme2 yusufhkran/bc4m_apiimage:0.1` komutuyla başlattım ve port yayını yaptım.

7. **Docker Hub'a İmaj Gönderme**
   - Docker imajını Docker Hub'a gönderdim.

8. **Kubernetes Cluster Oluşturma**
   - Google Cloud Platform (GCP) üzerinde 2 node içeren bir cluster oluşturdum.
   - Google Cloud Shell kullanarak cluster'a bağlandım ve `kubectl` komutlarıyla deployment işlemlerini gerçekleştirdim.

9. **Health Endpoint ve LoadBalancer**
   - /health endpoint'inin nasıl otomatik restart edilmesi gerektiği konusunda belirsizlik yaşadım. Bu kısmı geçtim.
   - `kubectl expose deployment bc4m-cluster --type LoadBalancer --port 5000 --target-port 5000` komutuyla LoadBalancer ekleyerek uygulamayı dış dünyaya açtım.

10. **Son Kontroller**
    - Servisin endpoint'ine erişim sağladım ve doğru yanıtı aldım.
    - Postman ile body'den gelen POST isteklerini gönderip, her şeyin düzgün çalıştığını kontrol ettim.

