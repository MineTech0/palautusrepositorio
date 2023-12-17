from kps_factory import KpsFactory


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

       
        try:
            KpsFactory.luo_peli(vastaus).pelaa()

        except AttributeError:
            break


if __name__ == "__main__":
    main()
