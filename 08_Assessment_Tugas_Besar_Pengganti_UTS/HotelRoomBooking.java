import java.util.Date;

public class HotelRoomBooking {
    private Pemesan pemesan;
    private String jenisKamar;
    private int jumlahTamu;
    private int jumlahMalam;
    private double hargaPerMalam;
    private String kodeVoucher;
    private boolean sudahDibayar;
    private Date tanggalCheckin;
    private Date tanggalCheckout;
    private boolean statusAktif;
    private static final int TAMBAHAN_TAMU_PER_ORANG = 100000;
    private static final int DISKON_VOUCHER = 50000;


    public HotelRoomBooking(Pemesan pemesan, String jenisKamar, int jumlahTamu, int jumlahMalam, double hargaPerMalam,
            Date tanggalCheckin, Date tanggalCheckout, boolean statusAktif,
            String kodeVoucher, boolean sudahDibayar) {

        this.pemesan = pemesan;
        this.jenisKamar = jenisKamar;
        this.jumlahTamu = jumlahTamu;
        this.jumlahMalam = jumlahMalam;
        this.hargaPerMalam = hargaPerMalam;
        this.tanggalCheckin = tanggalCheckin;
        this.tanggalCheckout = tanggalCheckout;
        this.statusAktif = statusAktif;
        this.kodeVoucher = kodeVoucher;
        this.sudahDibayar = sudahDibayar;
    }

    public void cetakDetailPemesanan() {
        System.out.println("===== DETAIL PEMESANAN KAMAR =====");
        System.out.println("Nama Pemesan : " + pemesan.getNama());
        System.out.println("Jenis Kelamin: " + pemesan.getJenisKelamin());
        System.out.println("No. KTP      : " + pemesan.getNomorKTP());
        System.out.println("Telepon      : " + pemesan.getNomorTelepon());
        System.out.println("Email        : " + pemesan.getEmail());        
        System.out.println("Jenis Kamar  : " + jenisKamar);
        System.out.println("Jumlah Tamu  : " + jumlahTamu);
        System.out.println("Jumlah Malam : " + jumlahMalam);
        System.out.println("Harga/Malam  : " + hargaPerMalam);
        System.out.println("Check-in     : " + tanggalCheckin);
        System.out.println("Check-out    : " + tanggalCheckout);
        System.out.println("Status Aktif : " + statusAktif);
        System.out.println("Voucher      : " + kodeVoucher);
        System.out.println("Sudah Dibayar: " + sudahDibayar);
        System.out.println("Total Biaya  : Rp " + hitungTotalBiaya());
        System.out.println("Tipe Tamu    : " + klasifikasiTamu());
        System.out.println("===================================");
    }


    public double hitungTotalBiaya() {
        double total = hargaPerMalam * jumlahMalam;
        if (jumlahTamu > 2) {
            total += (jumlahTamu - 2) * TAMBAHAN_TAMU_PER_ORANG;
        }
        if (kodeVoucher != null && kodeVoucher.length() > 3) {
            total -= DISKON_VOUCHER;
        }
        if (!statusAktif) {
            total = 0;
        }
        return total;
    }

    public String klasifikasiTamu() {
        if (jumlahTamu == 1)
            return "Individu";
        else if (jumlahTamu == 2)
            return "Pasangan";
        else
            return "Keluarga";
    }

    public String getJenisKamar() {
        return jenisKamar;
    }

    public void setJenisKamar(String jenisKamar) {
        this.jenisKamar = jenisKamar;
    }

    public int getJumlahMalam() {
        return jumlahMalam;
    }

    public void setJumlahMalam(int jumlahMalam) {
        this.jumlahMalam = jumlahMalam;
    }

    public double getHargaPerMalam() {
        return hargaPerMalam;
    }

    public void setHargaPerMalam(double hargaPerMalam) {
        this.hargaPerMalam = hargaPerMalam;
    }

    public boolean isSudahDibayar() {
        return sudahDibayar;
    }

    public void setSudahDibayar(boolean sudahDibayar) {
        this.sudahDibayar = sudahDibayar;
    }
}

