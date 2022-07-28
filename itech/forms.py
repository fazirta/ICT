from django.forms import ModelForm
from . import models


class PendaftaranValorantForm(ModelForm):
    class Meta:
        model = models.PendaftaranValorant
        fields = ['Nama_Tim', 'Nomor_Whatsapp_dan_Line', 'Nomor_Whatsapp_dan_Line_opsional', 'Player_1', 'Nama_Lengkap_atau_Nama_Asli_1', 'Player_2', 'Nama_Lengkap_atau_Nama_Asli_2', 'Player_3', 'Nama_Lengkap_atau_Nama_Asli_3',
                  'Player_4', 'Nama_Lengkap_atau_Nama_Asli_4', 'Player_5', 'Nama_Lengkap_atau_Nama_Asli_5', 'Player_6', 'Nama_Lengkap_atau_Nama_Asli_6', 'Paham_dan_ingin_berpartisipasi', 'Bukti_Transaksi', 'Bukti_Pelajar']

    def __init__(self, *args, **kwargs):
        super(PendaftaranValorantForm, self).__init__(*args, **kwargs)
        self.fields['Nama_Tim'].widget.attrs.update(
            {'placeholder': 'Nama Tim'})
        self.fields['Nomor_Whatsapp_dan_Line'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line'})
        self.fields['Nomor_Whatsapp_dan_Line_opsional'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line (opsional)'})
        self.fields['Player_1'].widget.attrs.update(
            {'placeholder': 'Player 1 (ex. ICT #1234)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_1'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Player_2'].widget.attrs.update(
            {'placeholder': 'Player 2 (ex. ICT #1234)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_2'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Player_3'].widget.attrs.update(
            {'placeholder': 'Player 3 (ex. ICT #1234)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_3'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Player_4'].widget.attrs.update(
            {'placeholder': 'Player 4 (ex. ICT #1234)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_4'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Player_5'].widget.attrs.update(
            {'placeholder': 'Player 5 (ex. ICT #1234)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_5'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Player_6'].widget.attrs.update(
            {'placeholder': 'Player 6 (cadangan)'})
        self.fields['Nama_Lengkap_atau_Nama_Asli_6'].widget.attrs.update(
            {'placeholder': 'Nama Lengkap atau Nama Asli'})
        self.fields['Paham_dan_ingin_berpartisipasi'].widget.attrs.update(
            {'placeholder': 'Saya memahami dan ingin berpartisipasi'})
        self.fields['Bukti_Transaksi'].widget.attrs.update(
            {'placeholder': 'Bukti Transaksi'})
        self.fields['Bukti_Pelajar'].widget.attrs.update(
            {'placeholder': 'Bukti Pelajar'})


class PendaftaranShortMovieForm(ModelForm):
    class Meta:
        model = models.PendaftaranShortMovie
        fields = ['Nama_Kelompok', 'Nama_Perwakilan', 'Nama_Anggota',
                  'Nomor_Whatsapp_dan_Line', 'Nomor_Whatsapp_dan_Line_opsional', 'Paham_dan_ingin_berpartisipasi', 'Bukti_Transaksi', 'Bukti_Pelajar']

    def __init__(self, *args, **kwargs):
        super(PendaftaranShortMovieForm, self).__init__(*args, **kwargs)
        self.fields['Nama_Kelompok'].widget.attrs.update(
            {'placeholder': 'Nama Kelompok'})
        self.fields['Nama_Perwakilan'].widget.attrs.update(
            {'placeholder': 'Nama Perwakilan'})
        self.fields['Nama_Anggota'].widget.attrs.update(
            {'placeholder': 'Nama Anggota [ Pisahkan dengan tanda koma (,) ] '})
        self.fields['Nomor_Whatsapp_dan_Line'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line'})
        self.fields['Nomor_Whatsapp_dan_Line_opsional'].widget.attrs.update(
            {'placeholder': 'Nomor Whatsapp dan Line (opsional)'})
        self.fields['Paham_dan_ingin_berpartisipasi'].widget.attrs.update(
            {'placeholder': 'Saya memahami dan ingin berpartisipasi'})
        self.fields['Bukti_Transaksi'].widget.attrs.update(
            {'placeholder': 'Bukti Transaksi'})
        self.fields['Bukti_Pelajar'].widget.attrs.update(
            {'placeholder': 'Bukti Pelajar'})
