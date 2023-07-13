from django.db import models

class PendaftaranValorant(models.Model):
    Nama_Tim = models.CharField(max_length=200, blank=False, null=False)
    Nomor_Whatsapp_dan_Line = models.CharField(
        max_length=200, blank=False, null=False)
    Nomor_Whatsapp_dan_Line_opsional = models.CharField(
        max_length=200, blank=True, null=True)
    Player_1 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_1 = models.CharField(
        max_length=200, blank=False, null=False)
    Player_2 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_2 = models.CharField(
        max_length=200, blank=False, null=False)
    Player_3 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_3 = models.CharField(
        max_length=200, blank=False, null=False)
    Player_4 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_4 = models.CharField(
        max_length=200, blank=False, null=False)
    Player_5 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_5 = models.CharField(
        max_length=200, blank=False, null=False)
    Player_6 = models.CharField(
        max_length=200, blank=False, null=False)
    Nama_Lengkap_atau_Nama_Asli_6 = models.CharField(
        max_length=200, blank=False, null=False)
    Paham_dan_ingin_berpartisipasi = models.BooleanField(default=False)
    Bukti_Transaksi = models.FileField()
    Bukti_Pelajar = models.FileField(null=True)

    def __str__(self):
        return self.Nama_Tim


class PendaftaranShortMovie(models.Model):
    Nama_Kelompok = models.CharField(max_length=200, blank=False, null=False)
    Nama_Perwakilan = models.CharField(max_length=200, blank=False, null=False)
    Nama_Anggota = models.CharField(max_length=200, blank=True, null=True)
    Nomor_Whatsapp_dan_Line = models.CharField(
        max_length=200, blank=False, null=False)
    Nomor_Whatsapp_dan_Line_opsional = models.CharField(
        max_length=200, blank=True, null=True)
    Paham_dan_ingin_berpartisipasi = models.BooleanField(default=False)
    Bukti_Transaksi = models.FileField()
    Bukti_Pelajar = models.FileField(null=True)

    def __str__(self):
        return self.Nama_Kelompok
