# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in = item.sell_in - 1

            if item.name == "Aged Brie":
                quality_increase = 1
                if item.sell_in < 0:
                    quality_increase = 2
                item.quality = min(item.quality + quality_increase, 50)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 10:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 5:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = 0
                continue

            if item.quality > 0:
                quality_decrease = 1
                if item.sell_in < 0:
                    quality_decrease = 2
                item.quality = max(item.quality - quality_decrease, 0)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
