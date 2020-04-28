# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class CelebritiesPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("mydatabase.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS celebrities_tb""")
        self.curr.execute("""create table celebrities_tb(
                Name text,
                career_high_point text,
                earnings_2019 integer,
                image_url text,
                number_of_times_on_forbes_list_since_2017 integer,
                profession text,
                profile text,
                source_of_income text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into celebrities_tb values (?,?,?,?,?,?,?,?)""", (
            item['Name'][0],
            item['career_high_point'][0],
            item['earnings_2019'][0],
            item['image_url'][0],
            item['number_of_times_on_forbes_list_since_2017'][0],
            item['profession'][0],
            item['profile'][0],
            item['source_of_income'][0]

        ))
        self.conn.commit()
