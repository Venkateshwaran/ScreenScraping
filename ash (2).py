from string import punctuation, whitespace
lis = [['Y10765227', '9884877926, 9283183326', '', 'Dealer', 'Rgmuthu'],
['L10038779', '9551154555', ',', ','],['R10831945', '9150000747, 9282109134, 9043728565', ',', ','],
['B10750123', '9952946340', '', 'Dealer', 'Bala'],
['R10763559', '9841280752, 9884797013', '', 'Dealer', 'Senthil']]
for item in lis:
 print ", ".join(a for a in item[1:] )