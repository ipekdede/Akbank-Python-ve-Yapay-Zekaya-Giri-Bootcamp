from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str, konum: Tuple[int, int]):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.konum = konum  # (x, y) koordinatı
        self.komsular: List[Tuple['Istasyon', int]] = []

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def __lt__(self, other):
        return self.idx < other.idx

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str, konum: Tuple[int, int]) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat, konum)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def aktarma_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int = 1) -> None:
        """Ortak istasyonlar arasında aktarma bağlantısı ekler"""
        self.baglanti_ekle(istasyon1_id, istasyon2_id, sure)


    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()

        while kuyruk:
            simdiki, yol = kuyruk.popleft()
            if simdiki.idx == hedef.idx:
                return yol
            ziyaret_edildi.add(simdiki.idx)

            for komsu, _ in simdiki.komsular:
                if komsu.idx not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu]))
                    ziyaret_edildi.add(komsu.idx)
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Istasyon nesnesi yerine sadece .idx'yi kullanıyoruz (karşılaştırılabilir bir string)
        pq = [(0, 0, baslangic.idx, [baslangic])]
        ziyaret_edildi = {}

        while pq:
            toplam_sure, _, _, yol = heapq.heappop(pq)
            simdiki = yol[-1]

            if simdiki.idx in ziyaret_edildi and ziyaret_edildi[simdiki.idx] <= toplam_sure:
                continue
            ziyaret_edildi[simdiki.idx] = toplam_sure

            if simdiki.idx == hedef.idx:
                return (yol, toplam_sure)

            for komsu, sure in simdiki.komsular:
                heapq.heappush(pq, (toplam_sure + sure, len(yol), komsu.idx, yol + [komsu]))

        return None

