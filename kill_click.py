from tkinter import *
from random import randint
from tkinter import Label

import pygame

list_point = []
with open('data_file/data_game.txt', 'r') as file:
    for i in file.readlines():
        list_point.append(int(i))
a = True
blood_point = list_point[0]
bones_point = list_point[1]
lvl_blood = list_point[2]
price_lvl_blood = list_point[3]
l_xp = list_point[4]
l_max_xp = list_point[5]
l_lvl = list_point[6]
lvl = list_point[7]
bones_plus = list_point[8]

skin_step1 = 0
skin_step2 = 0


def udar(event):
    global a, blood_point, bones_point, lvl, l_xp, l_lvl, l_max_xp, bones_plus
    if a:
        l_udar.configure(image=skin_playr_2)
        a = False
        musik = False
        knife_udar[randint(0, len(knife_udar) - 1)].play()
        l_xp += 1
        if lvl < 14:
            if l_xp >= mep_lvl(l_max_xp):
                l_xp = 0
                lvl += 1
            imege_lvl_bar.configure(width=lvl)
        else:
            lvl = 0
            l_lvl += 1
            l_max_xp += 50
            bones_plus += 1
            imege_lvl_bar.configure(width=lvl)
            lvl_label.configure(text=l_lvl)
    else:
        l_udar.configure(image=skin_playr_1)
        a = True
    point = randint(1, 6)
    if point == 6:
        blood_point += lvl_blood
        bones_point += bones_plus
        l_blood.configure(text=blood_point)
        l_boned.configure(text=bones_point)
    else:
        blood_point += lvl_blood
        l_blood.configure(text=blood_point)

    save()


def mep_lvl(number1):
    numberlvl = number1 / 14
    return numberlvl


def save():
    with open(r'data_file/data_game.txt', 'w') as file:
        file.write(str(f'{blood_point}\n'))
        file.write(str(f'{bones_point}\n'))
        file.write(str(f'{lvl_blood}\n'))
        file.write(str(f'{price_lvl_blood}\n'))
        file.write(str(f'{l_xp}\n'))
        file.write(str(f'{l_max_xp}\n'))
        file.write(str(f'{l_lvl}\n'))
        file.write(str(f'{lvl}\n'))
        file.write(str(f'{bones_plus}'))


def fun_shop(event):
    fon.place_forget()
    f_shop.configure(f_shop.place(x=0, y=0))
    shop_bl_point.configure(text=blood_point)
    shop_bo_point.configure(text=bones_point)


def fun_exit(event):
    fon.configure(fon.place(x=0, y=0))
    f_shop.place_forget()


def buy_up(event):
    global price_lvl_blood, blood_point, lvl_blood
    if blood_point >= price_lvl_blood:
        blood_point = blood_point - price_lvl_blood
        lvl_blood += 5
        if price_lvl_blood < 30000:
            price_lvl_blood += 300
        elif 30000 < price_lvl_blood < 50000:
            price_lvl_blood += 1000
        elif 50000 < price_lvl_blood < 100000:
            price_lvl_blood += 5000
        else:
            price_lvl_blood += 10000
        l_blood.configure(text=blood_point)
        shop_bl_point.configure(text=blood_point)
        price_up.configure(text=price_lvl_blood)


ruut = Tk()
ruut.title('Kill_clicker')
ruut.geometry('500x600')
ruut.resizable(width=False, height=False)
ruut.iconbitmap('image/image/icon.ico')

skin_playr_1 = ruut.photo_1 = PhotoImage(file='image/image/рука1.png')
skin_playr_2 = ruut.photo_2 = PhotoImage(file='image/image/рука2.png')
ruut.photo_shop = PhotoImage(file='image/image/магазин.png')
ruut.photo_interfase = PhotoImage(file='image/image/интерфейс2.png')
ruut.photo_box1 = PhotoImage(file='image/image/box1.png')
ruut.photo_box2 = PhotoImage(file='image/image/box2.png')

skin_1 = ruut.skin1 = PhotoImage(file='image/image_skin/skin_knife_1.png')
skin_1_2 = ruut.skin2 = PhotoImage(file='image/image_skin/skin_knife_2.png')
skin_2 = ruut.skin1 = PhotoImage(file='image/image_skin/skin_knife_cs_1.png')
skin_2_2 = ruut.skin2 = PhotoImage(file='image/image_skin/skin_knife_cs_2.png')
skin_3 = ruut.skin1 = PhotoImage(file='image/image_skin/skin_knife_legends1.png')
skin_3_2 = ruut.skin2 = PhotoImage(file='image/image_skin/skin_knife_legends2.png')
skin_4 = ruut.skin1 = PhotoImage(file='image/image_skin/skin_knife_ultra_1.png')
skin_4_2 = ruut.skin1 = PhotoImage(file='image/image_skin/skin_knife_ultra_2.png')
skin_5 = ruut.skin1 = PhotoImage(file='image/image_skin/скин ахотник.png')
skin_5_2 = ruut.skin1 = PhotoImage(file='image/image_skin/скин ахотник_2.png')
skin_6 = ruut.skin1 = PhotoImage(file='image/image_skin/скин pixel.png')
skin_6_2 = ruut.skin2 = PhotoImage(file='image/image_skin/скин pixel_2.png')
box_skin1 = ruut.box = PhotoImage(file='image/image/box2_skin1.png')
box_skin2 = ruut.box = PhotoImage(file='image/image/box2_skin2.png')
box_skin3 = ruut.box = PhotoImage(file='image/image/box2_skin3.png')
box_skin4 = ruut.box = PhotoImage(file='image/image/box2_skin4.png')
box_skin5 = ruut.box = PhotoImage(file='image/image/box2_ахотник.png')
box_skin6 = ruut.box = PhotoImage(file='image/image_skin/box2_pixel.png')
box_point = ruut.point = PhotoImage(file='image/image/box_resi.png')
skin_knife0 = ruut.menu_skin_photo = PhotoImage(file='image/image_skin/интерфейс для скина_нет.png')
skin_knife1 = ruut.knife_skin1 = PhotoImage(file='image/image_skin/интерфейс для скина_1.png')
skin_knife2 = ruut.knife_skin2 = PhotoImage(file='image/image_skin/интерфейс для скина_2.png')
skin_knife3 = ruut.knife_skin3 = PhotoImage(file='image/image_skin/интерфейс для скина_3.png')
skin_knife4 = ruut.knife_skin4 = PhotoImage(file='image/image_skin/интерфейс для скина_4.png')
skin_knife5 = ruut.knife_skin5 = PhotoImage(file='image/image_skin/интерфейс ахотник скин.png')
skin_knife6 = ruut.knife_skin6 = PhotoImage(file='image/image_skin/интерфейс pixel скин.png')
skin_list_skin = [skin_knife0, skin_knife1, skin_knife2, skin_knife3, skin_knife4, skin_knife5, skin_knife6]

box_list_drop = [box_skin1, box_skin2, box_skin3, box_skin4, box_skin5, box_skin6]

list_skin_playr1 = [skin_playr_1]
list_skin_playr2 = [skin_playr_2]
box_skins_list1 = [skin_1, skin_2, skin_3, skin_4, skin_5, skin_6]
box_skins_list2 = [skin_1_2, skin_2_2, skin_3_2, skin_4_2, skin_5_2, skin_6_2]
skin_list_menu = [skin_knife0]
with open('data_file/data_image.txt', 'r') as file:
    for i in file.readlines():
        list_skin_playr1.append(box_skins_list1[int(i)])
        list_skin_playr2.append(box_skins_list2[int(i)])
        skin_list_menu.append(skin_list_skin[int(i) + 1])

pygame.init()
knife_udar_1 = pygame.mixer.Sound('audio/udar_1.mp3')
knife_udar_2 = pygame.mixer.Sound('audio/udar_2.mp3')
knife_udar_3 = pygame.mixer.Sound('audio/udar_3.mp3')
knife_udar_4 = pygame.mixer.Sound('audio/udar-nojom-4.mp3')
knife_udar_5 = pygame.mixer.Sound('audio/otrez-palec-nojom.mp3')
knife_1 = pygame.mixer.Sound('audio/vynuli-noj-cs-go.mp3')
knife_2 = pygame.mixer.Sound('audio/zasunuli-mech-v-nozhny.mp3')
fon_music = pygame.mixer.Sound('audio/muzika-bez-ap-6.mp3')
fon_music.set_volume(0.3)

knife_udar_1.set_volume(0.3)
knife_udar_2.set_volume(0.3)
knife_udar_3.set_volume(0.3)
knife_1.set_volume(0.3)
knife_2.set_volume(0.3)

knife_udar = [knife_udar_1, knife_udar_2, knife_udar_3, knife_udar_4, knife_udar_5]


list_name_skin = ['knife']

list_name_skins = ['stationery killer', 'kitchen knife', 'drunk dragon', 'bald man tooth', 'hunter', 'pixel']

with open('data_file/data_name.txt', 'r') as file:
    for i in file.readlines():
        list_name_skin.append(i.replace('\n', ''))


fon = Frame(ruut, width=500, height=600, bd=0)
fon.place(x=0, y=0)

l_fon = Label(fon, image=ruut.photo_interfase, bd=0, )
l_fon.place(x=0, y=0)

f_udar = Frame(fon, width=500, height=400, bd=0)
l_udar = Label(f_udar, image=ruut.photo_interfase, bd=0)
l_udar.bind("<Button-1>", udar)


def fun_knife_on(event):
    l_udar.configure(image=skin_playr_1)
    knife_1.play()


def fun_knife_off(event):
    l_udar.configure(image=ruut.photo_interfase)
    knife_2.play()


l_udar.bind("<Enter>", fun_knife_on)
l_udar.bind("<Leave>", fun_knife_off)
f_udar.place(x=0, y=180)
l_udar.place(x=0, y=-180)

l_blood = Label(fon, text=blood_point, font=("Comic Sans MS", 10), bg='#ffff00')
l_boned = Label(fon, text=bones_point, font=("Comic Sans MS", 10), bg='#ffff00')
l_blood.place(x=60, y=60)
l_boned.place(x=60, y=115)

lvl_frame = Frame(ruut, width=200, height=35)
image_lvl = Label(lvl_frame, image=ruut.photo_interfase, bd=0, bg='#aaaa0a')
lvl_label = Label(lvl_frame, text=l_lvl, font=('Comic Sans MS', 15), bg='#aaaa0a')
imege_lvl_bar = Label(lvl_frame, bd=0, bg='#02e8eb', width=lvl, height=1)
lvl_frame.place(x=0, y=0)
image_lvl.place(x=0, y=0)
lvl_label.place(x=27, y=10)
imege_lvl_bar.place(x=80, y=15)

f_shop = Frame(ruut, width=500, height=600)
l_shop = Label(f_shop, image=ruut.photo_shop, bd=0)
l_f_shop = Frame(f_shop, bg='red')
f_shop.place_forget()
l_shop.place(x=0, y=0)

btn_shop = Label(fon, text='Shop', font=("Comic Sans MS", 15), bg='#ffff00')
btn_shop.bind("<Button-1>", fun_shop)
btn_shop.place(x=415, y=75)

btn_exit = Label(f_shop, text='Exit', font=("Comic Sans MS", 15), bg='#c5c524', width=7, height=1)
btn_exit.bind("<Button-1>", fun_exit)
btn_exit.place(x=363, y=515)

shop_bl_point = Label(f_shop, text=blood_point, font=("Comic Sans MS", 10), bg='#c5c524')
shop_bo_point = Label(f_shop, text=bones_point, font=("Comic Sans MS", 10), bg='#c5c524')
shop_bl_point.place(x=120, y=50)
shop_bo_point.place(x=315, y=50)

btn_shop1 = Label(f_shop, text='Buy', font=("Comic Sans MS", 15), bg='#c5c524', width=10)
btn_shop1.bind("<Button-1>", buy_up)
btn_shop1.bind("<Enter>", lambda event: btn_shop1.configure(font=("Comic Sans MS Bold", 15)))
btn_shop1.bind("<Leave>", lambda event: btn_shop1.configure(font=("Comic Sans MS", 15)))
price_up = Label(f_shop, text=price_lvl_blood, font=("Comic Sans MS", 15), bg='#c5c524')
price_up.place(x=293, y=178)

btn_shop1.place(x=272, y=125)

btn_shop2 = Label(f_shop, text='Buy box', font=("Comic Sans MS", 15), bg='#c5c524')
btn_shop2.bind("<Enter>", lambda event: btn_shop2.configure(font=("Comic Sans MS Bold", 15)))
btn_shop2.bind("<Leave>", lambda event: btn_shop2.configure(font=("Comic Sans MS", 15)))

prise_box = Label(f_shop, text=200, font=("Comic Sans MS", 15), bg='#c5c524')
prise_box.place(x=293, y=290)


def open_box(event):
    global list_skin_playr1, list_skin_playr2, box_skins_list1, box_skins_list2, skin_list_menu, skin_list_skin, blood_point, bones_point, box_list_drop
    if bones_point >= 200:
        bones_point -= 200
        int_skin = randint(0, len(box_skins_list1) - 1)
        if box_skins_list1[int_skin] in list_skin_playr1:
            int_blood = randint(2000, 5000)
            blood_point += int_blood
            if int_blood > 4000:
                int_bones = randint(30, 300)
                bones_point += int_bones
                l_boned.configure(text=bones_point)
            l_blood.configure(text=blood_point)
            open_box_l.configure(image=box_point)

        else:
            list_skin_playr1.append(box_skins_list1[int_skin])
            list_skin_playr2.append(box_skins_list2[int_skin])
            skin_list_menu.append(skin_list_skin[int_skin + 1])
            open_box_l.configure(image=box_list_drop[int_skin])
            with open('data_file/data_image.txt', 'a') as filee:
                filee.write(f'{int_skin}\n')
            with open('data_file/data_name.txt', 'a') as filee:
                filee.write(f'{list_name_skins[int_skin]}\n')
                list_name_skin.append(list_name_skins[int_skin])
        box.configure(box.place(x=0, y=0))
        f_shop.place_forget()
        l_boned.configure(text=bones_point)


def open_box_skin(event):
    box1.configure(image=ruut.photo_box2)
    exit_box.place(x=0, y=0)


def exit_boxi(event):
    box1.configure(image=ruut.photo_box1)
    exit_box.place_forget()
    box.place_forget()
    drop.place_forget()
    fun_shop(event)


btn_shop2.bind("<Button-1>", open_box)
btn_shop2.place(x=294, y=237)
box = Frame(ruut, width=500, height=600)
box1 = Label(box, image=ruut.photo_box1, bd=0)
box1.bind("<Button-1>", open_box_skin)
box.place_forget()
box1.place(x=0, y=0)
exit_box = Frame(box, width=500, height=600)
open_box_l = Label(exit_box, image=ruut.photo_box2, bd=0)
open_box_l.bind("<Button-1>", exit_boxi)
open_box_l.place(x=0, y=0)
exit_box.place_forget()
box_drop = Frame(box, width=200, height=200)
drop = Label(box_drop, bd=0)
drop.place(x=-200, y=-200)
box_drop.place_forget()

menu_skin = Frame(ruut, width=500, height=600)
menu_skin_l = Label(menu_skin, image=ruut.menu_skin_photo, bd=0)
btn_f_skin = Frame(fon, width=100, height=50)
btn_l_skin = Label(btn_f_skin, image=ruut.photo_interfase, bd=0)
btn_l_skin.bind("<Button-1>", lambda event: menu_skin.configure(menu_skin.place(x=0, y=0)))
btn_f_skin.place(x=315, y=9)
btn_l_skin.place(x=-315, y=-9)
menu_skin.place_forget()
menu_skin_l.place(x=0, y=0)


def fun_dress(event):
    global list_skin_playr1, list_skin_playr2, skin_step1, skin_step2, skin_playr_1, skin_playr_2
    skin_playr_1 = list_skin_playr1[skin_step1]
    skin_playr_2 = list_skin_playr2[skin_step2]
    menu_skin.place_forget()


def slide_r(event):
    global skin_step1, skin_step2, skin_list_menu, list_name_skin
    if skin_step1 < skin_list_menu.index(skin_list_menu[-1]):
        skin_step1 += 1
        skin_step2 += 1
        skin_l.configure(image=skin_list_menu[skin_step1])
        name_skin_label.configure(text=list_name_skin[skin_step1])


def slide_l(event):
    global skin_step1, skin_step2, skin_list_menu
    if skin_step1 > skin_list_menu.index(skin_list_menu[0]):
        skin_step1 -= 1
        skin_step2 -= 1
        skin_l.configure(image=skin_list_menu[skin_step1])
        name_skin_label.configure(text=list_name_skin[skin_step1])


btn_slide1 = Frame(menu_skin, width=55, height=100)
btn_slide2 = Frame(menu_skin, width=55, height=100)
btn_skin = Frame(menu_skin, width=205, height=85)
btn_skin_l = Label(btn_skin, image=ruut.menu_skin_photo, bd=0)
btn_skin_l.bind("<Button-1>", fun_dress)
btn_slide1_l = Label(btn_slide1, image=ruut.menu_skin_photo, bd=0)
btn_slide1_l.bind("<Button-1>", slide_l)
btn_slide2_l = Label(btn_slide2, image=ruut.menu_skin_photo, bd=0)
btn_slide2_l.bind("<Button-1>", slide_r)
skin_f = Frame(menu_skin, width=270, height=300)
skin_l = Label(skin_f, image=ruut.menu_skin_photo)
name_skins_frame = Frame(menu_skin, width=345, height=88)
name_skin_image = Label(name_skins_frame, image=ruut.menu_skin_photo, bd=0)
name_skin_label = Label(name_skins_frame, text='knife', font=("Comic Sans MS", 30), bg='#b5b50b')

name_skins_frame.place(x=77, y=497)
name_skin_image.place(x=-77, y=-497)
name_skin_label.place(relx=0.5, rely=0.5, anchor=CENTER)
skin_f.place(x=115, y=150)
skin_l.place(x=-115, y=-150)

btn_skin.place(x=150, y=10)
btn_skin_l.place(x=-150, y=-10)
btn_slide1_l.place(x=-20, y=-250)
btn_slide2_l.place(x=-425, y=-250)
btn_slide2.place(x=425, y=250)
btn_slide1.place(x=20, y=250)

btn_menu_pauze = Frame(fon, width=65, height=65)
btn_menu_pauze_l = Label(btn_menu_pauze, bd=0, image=ruut.photo_interfase)
btn_menu_pauze_l.bind("<Button-1>", lambda event: menu_pauze.place(x=0, y=0))
btn_menu_pauze.place(x=430, y=3)
btn_menu_pauze_l.place(x=-430, y=-3)


def exit_game(event):
    save()
    exit()


ruut.menu_pauze_ft = PhotoImage(file='image/image/_menu_.png')
menu_pauze = Frame(ruut, width=500, height=600)
menu_pauze_l = Label(menu_pauze, image=ruut.menu_pauze_ft, bd=0)
btn_menu_cnt = Label(menu_pauze, text='continue', font=("Comic Sans MS", 30), bg='#9a9a2c', width=8, height=1)
btn_menu_ext = Label(menu_pauze, text='exit', font=("Comic Sans MS", 30), width=7, bg='#9a9a2c')
btn_menu_cnt.bind("<Button-1>", lambda event: menu_pauze.place_forget())
btn_menu_ext.bind("<Button-1>", exit_game)
btn_menu_cnt.bind("<Enter>", lambda event: btn_menu_cnt.configure(font=('Comic Sans MS Bold', 30)))
btn_menu_cnt.bind("<Leave>", lambda event: btn_menu_cnt.configure(font=('Comic Sans MS', 30)))
btn_menu_ext.bind("<Enter>", lambda event: btn_menu_ext.configure(font=('Comic Sans MS Bold', 30)))
btn_menu_ext.bind("<Leave>", lambda event: btn_menu_ext.configure(font=('Comic Sans MS', 30)))

menu_pauze_l.place(x=0, y=0)
btn_menu_cnt.place(x=155, y=145)
btn_menu_ext.place(x=167, y=240)


fon_music.play(-1)
ruut.mainloop()
