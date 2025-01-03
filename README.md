Burada maşın öyrənmə üsullarından istifadə edərək B(E2) kimi xüsusiyyətlər, deformasiya parametrləri və əlaqəli səhvlər daxil olmaqla, çatışmayan nüvə məlumatlarını proqnozlaşdırmaq üçün istifadə olunan prosesi təsvir edəcəyik. 
Məlumatlar dəstinin araşdırılması:
Xüsusiyyətlər: (Z) (atom sayı), (N) (neytron sayı), (A) (kütlə sayı), (E(keV)) və digər xüsusiyyətlər;
Hədəflər: (B(E2) (e2b2)), (ps), (β2) və onların müvafiq xətaları.

Maşın Öyrənməsindən istifadə edərək çatışmayan nüvə məlumatlarının proqnozlaşdırılmasında aşağıdakı mərhələlərə baxacağıq:
1.	Məlumatların emal edilməsi - Xüsusiyyətlərdə çatışmayan dəyərlər ədədi ortadan istifadə etməklə hesablanmalı,təlim modellərini işə salmaq üçün müvafiq sütunlar seçilməlidir.
2.	Model təlimi - Məlumat dəstində çatışmayan hər bir sütun üçün ayrıca reqressiya modelləri (Random Forest Regressor) öyrədilir.Z, N, A və (E(keV)) kimi xüsusiyyətlər proqnozlaşdırıcı kimi istifadə edilmişdir.
3.	Proqnozlaşdırma - Modellər hər bir hədəfin tapılması məqsədilə çatışmayan dəyərləri proqnozlaşdırmaq üçün istifadə edilmişdir. Proqnozlaşdırılan dəyərlər v 5. 
4.	 Nəticə - Bütün çatışmayan dəyərlər doldurulmaqla tam verilənlər toplusu yaradıldı. Yenilənmiş məlumat dəsti sonrakı istifadə üçün saxlandı, verilənlər bazasına yenidən inteqrasiya edildi.

