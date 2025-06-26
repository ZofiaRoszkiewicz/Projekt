def pokaz_osoby_dla_ksiegarni(typ):
    idx = listbox_ksiegarnie.curselection()
    if not idx:
        return
    ksiegarnia = ksiegarnie[idx[0]]
    nazwa = ksiegarnia.nazwa
    dane = ksiegarnia_pracownicy if typ == "pracownik" else ksiegarnia_klienci
    osoby = dane.get(nazwa, [])
    for o in osoby:
        if o.marker:
            o.marker.delete()
        o.marker = map_widget.set_marker(
            o.latitude,
            o.longitude,
            text=f"{o.imie_nazwisko}\n({o.miasto})"
        )
    if osoby:
        lat = sum(o.latitude for o in osoby) / len(osoby)
        lon = sum(o.longitude for o in osoby) / len(osoby)
        map_widget.set_position(lat, lon)
        map_widget.set_zoom(7)






