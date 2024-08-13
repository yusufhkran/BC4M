##                                              Proje Hazırlama Raporu
## Uygulama Erişim linki= [text](http://www.bcfmapi.cloud/)
## Bu yazıyı projeyi tamamladıktan sonra proje ve BC4M hakkındaki fikirlerimi belirtmek adına yazdığımı belirtmek istiyorum. Bu güzel çalışmayı ve devops u detaylıca öğrenme konusunda çok değerli olan bu akademiyi düzenleyen herkese çok teşekkür ediyorum. Ek olarak kendini kanıtlamaya çalışan, teorik bilgilerini pratiğe dökemeyen ve kariyerinde sıçrama yapmak için çabalayan öğrencilere verdiğiniz değerden dolayı tekrardan teşekkür ederim.
0. **Projeyi oluştururken izlediğim adımlar:**
1. **API yazma adımlarım**
   - İlk olarak GÖREVLER kısmındaki ilk adımı okuyup yapmam gerekenleri okuyup daha sonra işe koyuldum. İlk iş olarak API hakkındaki bilgilerimi geliştirmem gerektiğini düşündüm.
   - Daha önce herhangi bir API yazmadığım için case ile tanıştığım ilk gün olan 09/08/2024 gününü API hakkında bilgi edinme ve kullanacağım yazılım dilini seçmeye ayırdım.
   - API nedir? Ne işe yarar? Nasıl yazılır? gibi sorulara cevap buldum ve sırada seçeceğim yazılım dili vardı.
   - Daha önce herhangi bir yazılım dilinde uzmanlaşmadığım için bir API yazmak benim için ilk bakışta en zor görünen görevdi. Bu yüzden daha önceden tanışma fırsatım olan ve giriş seviyede sayılabilecek kadar bilgi sahibi olduğum GOLANG dilini seçtim.
   - Daha sonra işe koyulup GOLANG ile API yazmaya çalıştım.
   - Bu dilde yeteceğini düşündüğüm GOLANG bilgim maalesef yetersiz oldu ve uzun saatler sonucunda seçimimin yanlış olduğunu fark ettim. Bana tanınan süreyi değerli kullanmak istememden dolayı vaktimi GOLANG öğrenmek ile kaybetmek istemedim.
   - Bir süre daha düşünüp zayıf olduğum bir konuyu en basit şekilde atlatmam gerektiğini düşündüm ve uygulamayı Python ile yazmaya karar verdim.
   - Yaklaşık 4 saatimi alan çalışmam ve araştırmam sonucu 10 Ağustos günü sabaha karşı bir saatte ilk görevimi bitirdim.
   - Postman aracılığıyla gönderdiğim istekler sonucu birinci görevdeki isterler karşılanmış oldu.
2. **Dockerfile oluşturma adımlarım**
   - Case’in ikinci kısmında benden istenen bir Docker file yazmamdı. Daha önce Docker üzerinde kendimi geliştirmiş olmam işime fazlasıyla yaradı. Başlar başlamaz Docker file yazamayacak durumda olsam da bir iki saatlik konu tekrarı ile bu dosyayı yazabileceğimin farkındaydım.
   - Çalışmalarıma başlayınca ilk işim daha önce aldığım Udemy kursundaki Docker file ile ilgili videoları izlemek oldu.
   - Kursumdaki kaynakları tüketip daha sonra Medium ve YouTube üzerinden bildiklerimi ve yeni öğrendiklerimi pekiştirip başarılı bir Docker file yazdım.
   - Docker file oluştururken ki adımlarım:
     - Bu imajda koşturacak olan container'ların üzerinde çalışacağı işletim sistemini ve yazılımını `FROM` ile Python ve Linux Alpine tabanlı imajını seçtim.
     - `WORKDIR`ile app dosyası açıp COPY ile projedeki dosyaları buraya kopyaladım.
     - `RUN pip install -r requirements.txt` ile projedeki Flask gibi bağımlılıkları projeye indirdim.
     - `EXPOSE` ile 5000 portuna publish ettim ve son olarak `CMD` ile programı çalıştırma komutunu girdim.
3. **Dockerfile ile oluşturduğum image ı Docker Hub a gönderme aşamalarım** 
   - Daha sonra oluşturduğum Docker file ile bir image oluşturma adımına geçtim. Docker mantığını daha önceden biliyor olmak bana fazlasıyla vakit kazandırmıştı ve çok kısa bir araştırmayla image oluşturma işlemini tamamladım.
   - `docker build -t yusufhkran/bc4m_apiimage:0.1 .` kodu ile image oluşturulmuş oldu.
   - Daha sonra bu imajdan container oluşturdum.
   - Container için kullandığım kod:  
     - `docker container run -d --name bc4m_apideneme1 yusufhkran/bc4m_apiimage:0.1`
   - Container detach bir şekilde başlatıldıktan sonra local adresim 127.0.0.1 adresinin 5000 portuna giriş yapmama rağmen bağlantıda sorun yaşamıştım.
   - Bu adrese bağlanamıyordum ve sorunun ne olduğu hakkında hiç bir fikrim yoktu. Bu kısımda herhangi bir yerden bir ipucu bulamadığım için yapay zekadan destek aldım ve sorunun Docker file veya Docker ile herhangi bir alakası yoktu. Burada kısmın programı yazarken programın dış dünyaya kapalı olduğunu fark ettim.
   - Bu sorunun çözümünü "Python Flask uygulamasını dış dünyaya nasıl açarım?" başlığıyla araştırmaya başladım.
   - Bu hatayı programı yazarken fark etmememin sebebinin ise Pycharm üzerinden yaptığım denemelerde herhangi bir sorun yaşamamam olduğunun farkına vardım.
   - `app.run(debug=True)` şeklinde olan uygulama başlangıcını `app.run(debug=True, host="0.0.0.0", port=5000)` olarak değiştirdim.
   - Bu değişiklikten sonra eski image üzerinde değişiklik olduğu için aynı Docker file ile yeni bir image oluşturdum.
   - Yeni oluşturduğum bu image ile yeni bir container daha oluşturdum ve yine aynı sorunla karşılaştım.
   - Daha sonra sorunun üzerine tekrardan yoğunlaşıp nedenini anlamaya çalıştım.
   - Docker üzerine kurs almış olmamın olumlu etkisi tekrar devreye girip container oluştururken oluşturduğumuz container'a port publish edilebildiğini anımsayıp bu alanda araştırma yapmaya karar verdim.
   - Tekrardan Udemy kursuma dönüp bu konu hakkında videoları izlemeye başladım. İzledikten sonra ise `-p 5000:5000` komutunun container'ın içindeki 5000 portunu benim makinemdeki 5000 portuna bağlayabileceğinin farkına vardım.
   - Sırada tekrardan bir container oluşturmak vardı ve `docker container run -d -p 5000:5000 --name bc4m_apideneme2 yusufhkran/bc4m_apiimage:0.1` kodu ile container başarılı bir şekilde oluşturuldu.
   - Bu işlemden sonra image'i Docker Hub'a gönderdim.
4. **Kubernetes Cluster kurma adımlarım**
   - Sırada 4. görev olan Cluster oluşturma görevi vardı. Önce cluster'ın ne olduğunu iyice araştırdım. Daha sonra projeyi deploy edeceğim Kubernetes cluster'ını hangi platformda oluşturacağımı seçme kısmına geldim.
   - Bu aşamada aklıma ilk olarak daha önceden de ilgi duyduğum platform olan Amazon Web Services geldi fakat AWS üzerinde cluster oluşturmak ücretli olduğu için diğer seçenekleri değerlendirmeye aldım. Kubernetes'in yaratıcısı olması sebebiyle Google Cloud Platform, Microsoft Azure'a göre daha çok ilgimi çekti ve GCP üzerinden ilerlemeye karar verdim.
   - Burada ilk adım olarak GCP hesabıma giriş yaptım ve bir container deploy etme için gereken cluster için gerekenleri araştırdım.
   - Araştırmalardan sonra 2 node içeren us-central1-c bölgesine ait bir cluster oluşturdum. 
5. **Kubernetes Cluster a uygulama deploy etme adımlarım**
   - Cluster oluşturma kısmı çok fazla zor olmamıştı. Beni asıl zorlayan kısım image'i deploy etmek oldu.
   - Deploy kısmında izlediğim adımlar:
     - İlk olarak GCP dokümantasyonu eşliğinde Google Cloud Shell'i bilgisayarıma kurdum.
     - Daha sonra buradan cloud hesabıma giriş yaptım ve YouTube üzerinden bir örneği uygulamaya çalıştım.
     - Oluşturduğum cluster'a girip "connect" kısmında yazan bağlantı ile shell üzerinden cluster'a bağlandım.
     - Cluster'a bağlandıktan sonra shell üzerinden kubectl aracı ile deployment yarattım.
      - `kubectl create deployment bc4m-cluster --image=yusufhkran/bc4m_apiimage:0.1`
     - "Uygulama Deploymentı" görevinin ilk kısmını tamamlamış oldum fakat ikinci kısımda istenen "/health endpointinin cevap vermediği durumda uygulama otomatik restrart olmalı" kısmını anlayamadım. Uygulama çalışır durumda ve neden cevap vermemesi gerektiğini ve uygulamanın restart kısmının uygulamanın yazılımıyla mı restart edilecekti yoksa cluster'la mı restart edilecekti anlayamadığım için bu kısmı askıya aldım ve son görevle yoluma devam ettim.
6. **Uygulamaya LoadBalancer expose etme adımlarım**
   - Son görevdeki loadBalancer ekleme kısmının çözümünü uzun bir araştırmanın sonunda GCP dokümantasyonunda buldum.
   - Bu çözümün benim istediğim çözüm olduğunu dokümantasyonlardaki adımları izleyip benim uyguladığım adımlarla aynı olduğunu fark edince uygulamaya koyuldum.
   - "kubectl expose deployment hello-server --type LoadBalancer --port 80 --target-port 8080"
   - Dokümantasyonda bulduğum bu shell kodunu kendi uygulamama hizmet edecek şekilde değiştirdim ve son hali `kubectl expose deployment bc4m-cluster --type LoadBalancer --port 5000 --target-port 5000` oldu.
   - Burada cluster'a gönderdiğim LoadBalancer türündeki servis sayesinde uygulamam dış dünyaya açıldı.
   - Son olarak "Gateways, Services & Ingress" kısmından oluşturduğum servisin endpoint kısmından oluşturulan IP adresine giriş yaptım ve {"msg": "BC4M"} yazısını gördüm. /health isteği gönderip durumunu kontrol ettim. Postman ile body'den post istekleri atıp kontrolleri gerçekleştirdim ve herhangi bir sorunlarla karşılaşmadım.
