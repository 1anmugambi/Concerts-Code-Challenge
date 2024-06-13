class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        venue._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
        band._concerts.append(self)
        venue._concerts.append(self)

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    def concerts(self):
        return self._concerts

    def bands(self):
        return list({concert.band for concert in self._concerts})
