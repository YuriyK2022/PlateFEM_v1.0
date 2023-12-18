# АНАЛИТИЧЕСКИЙ И ЧИСЛЕННЫЙ АНАЛИЗ ИЗГИБА КРУГЛОЙ ТРЕХСЛОЙНОЙ
# ПЛАСТИНЫ ПОД ДЕЙСТВИЕМ ЛОКАЛЬНЫХ НАГРУЗОК СРЕДСТВАМИ ИНЖЕНЕРНО-ПРОГРАМАМНОГО
# КОМПЛЕКСА ANSYS, СПЕЦИАЛИЗИРОВАННОГО ПАКЕТА PYMAPDL И ЯЗЫКА ПРОГРАММИРОВАНИЯ
# PYTHON

# РЕАЛИЗОВАНО:
# 1. Задача осесимметричного поперечного изгиба трехслойной круглой пластины
#    в линейной постановке.
# 2. Задача осесимметричного изгиба однослойной круглой пластины 
#    в линейной и нелинейной постановке.

__version__ = 'v1.0'
from tkinter import*
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
from tkinter.scrolledtext import ScrolledText
import os
import keyboard
from ansys.mapdl.core import launch_mapdl

# MAIN PROGRAM FUNCTIONS
# define Ansys UNITS
def f_sel_Units_SI():
    units_SI = mapdl.units("SI")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, units_SI)
    t2_solver.yview(END)

def f_sel_Units_MKS():
    units_MKS = mapdl.units("MKS")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, units_MKS)
    t2_solver.yview(END)

def f_sel_Units_uMKS():
    units_uMKS = mapdl.units("uMKS")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, units_uMKS)
    t2_solver.yview(END)

def f_sel_Units_US_ft():
    units_USft = mapdl.units("BFT")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, units_USft)
    t2_solver.yview(END)

def f_sel_Units_US_in():
    units_USin = mapdl.units("BIN")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, units_USin)
    t2_solver.yview(END)


def f_kps_plot():
        mapdl.kplot(vtk = True,
                    show_keypoint_numbering = True,
                    render_points_as_spheres = False,
                    background = "grey",
                    show_bounds = False,
                    font_size = 10
                    )

def f_lns_plot():
    mapdl.lplot(vtk = True,
                show_keypoint_numbering = False,
                show_line_numbering = True,
                background = "grey",
                show_bounds = False,
                show_axes = True,
                font_size = 10,
                color_lines = True,
                line_width=5,
                cpos="iso",
                )

def f_ars_plot():
     mapdl.aplot(vtk = True,
                 quality = 9,
                 show_area_numbering = True,
                 show_line_numbering = False,
                 color_areas = True,
                 background = "grey",
                 show_bounds = False,
                 show_axes = True,
                 show_lines = True,
                 cpos = "iso"
                 )

def f_vol_plot():
     mapdl.vplot(vtk = True,
                 quality = 9,
                 show_volume_numbering = True,
                 show_area_numbering = False,
                 show_line_numbering = False,
                 color_areas = False,
                 show_lines = True,
                 background = "grey",
                 show_bounds = False,
                 show_axes = True,
                 cpos = "iso"
                 )

def f_elem_plot():
    mapdl.eplot(vtk = True,
                show_node_numbering = False,
                plot_bc = True,
                plot_bc_legend = True,
                plot_bc_labels = True,
                bc_labels = ['UX', 'UY', 'UZ', 'FX', 'FY', 'FZ'],
                show_edges=True,
                smooth_shading=True,
                background = "grey",
                show_axes = True,
                cpos = "iso"
                )

def f_node_plot():
    mapdl.nplot(vtk = True,
                nnum = False,
                plot_bc = True,
                plot_bc_legend = True,
                plot_bc_labels = True,
                bc_labels = ['UX', 'UY', 'UZ', 'FX', 'FY', 'FZ'],
                show_edges=True,
                smooth_shading=True,
                background = "grey",
                show_axes = True,
                cpos = "iso"
                )


def f_kps_del_all():
    kps_del_all = mapdl.kdele("ALL")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, kps_del_all)
    t2_solver.yview(END)

def f_lns_del_all():
    lns_del_all = mapdl.ldele("ALL", kswp = 0)
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, lns_del_all)
    t2_solver.yview(END)

def f_ars_del_all():
    ars_del_all = mapdl.adele("ALL", kswp = 0)
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, ars_del_all)
    t2_solver.yview(END)

def f_vol_del_all():
    vol_del_all = mapdl.vdele("ALL", kswp = 0)
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, vol_del_all)
    t2_solver.yview(END)  


def f_kps_list():
    kps_list = mapdl.klist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, kps_list )
    t1_output.yview(END)

def f_lns_list():
    lns_list = mapdl.llist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, lns_list)
    t1_output.yview(END)

def f_ars_list():
    ars_list = mapdl.alist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, ars_list)
    t1_output.yview(END)

def f_vol_list():
    vol_list = mapdl.vlist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, vol_list)
    t1_output.yview(END)

def f_elem_list():
    elem_list = mapdl.elist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, elem_list)
    t1_output.yview(END)

def f_elem_etlist():
    elem_etlist = mapdl.etlist("ALL")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, elem_etlist)
    t1_output.yview(END)

def f_mat_list():
    mat_list = mapdl.mplist("ALL", "", "", "", "EVLT")
    t1_output.insert(END, "\n" )
    t1_output.insert(END, "\n" )
    t1_output.insert(END, mat_list)
    t1_output.insert(END, "\n" )
    t1_output.yview(END)



def f_kps_sel_pick():
    kps_sel_pick = mapdl.ksel("S", "P")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selected Picked Keypoints: ")
    t2_solver.insert(END, kps_sel_pick)
    t2_solver.yview(END)

def f_kps_sel_atch_lines():
    kps_sel_atch_lines = mapdl.ksll("S")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selected Keypoints attached to Lines: ")
    t2_solver.insert(END, kps_sel_atch_lines)
    t2_solver.yview(END)

def f_kps_sel_loc():
    win_sel_loc = Toplevel()
    win_sel_loc.title("Select Keypoints by Location")
    win_sel_loc.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_sel_loc.winfo_screenwidth()
    h1 = win_sel_loc.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 65
    win_sel_loc.geometry('450x130+{}+{}'.format(w1, h1))
    win_sel_loc.resizable(False, False)

    def f_clear(event):
        ent_loc.delete(0, END)
        ent_loc.focus()
        var.set(0)
        
    def f_destroy(event):
        ent_loc.delete(0, END)
        win_sel_loc.destroy()
    
    def f_set_loc_OK(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.ksel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 1:
            location_y = mapdl.ksel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 2:
            location_z = mapdl.ksel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)
            win_sel_loc.destroy()
    
    def f_set_loc_apply(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.ksel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
        elif var.get() == 1:
            location_y = mapdl.ksel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
        elif var.get() == 2:
            location_z = mapdl.ksel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of keypoints by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)

    lab001 = Label(win_sel_loc, text = "[KSEL] Selects a subset of keypoints by Location")
    lab001.grid(row = 1, columnspan = 2, sticky = W, padx = 5, pady = 5)

    var = IntVar()
    var.set(0)

    loc_x = Radiobutton(win_sel_loc,
                        text = 'Location X',
                        variable = var,
                        value = 0
                        )
    loc_x.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    loc_y = Radiobutton(win_sel_loc,
                        text = 'Location Y',
                        variable = var,
                        value = 1
                        )
    loc_y.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)

    loc_z = Radiobutton(win_sel_loc,
                        text = 'Location Z',
                        variable = var,
                        value = 2
                        )
    loc_z.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    ent_loc = Entry(win_sel_loc, width = 10)
    ent_loc.grid(row = 2, column = 3, sticky = W, padx = 5, pady = 5)
    ent_loc.focus()

    btn001 = Button(win_sel_loc,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_sel_loc,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_sel_loc,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 3, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_sel_loc,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 3, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_set_loc_OK)
    btn002.bind('<Button-1>', f_set_loc_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_lns_sel_pick():
    lns_sel_pick = mapdl.lsel("S", "P")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selected Picked Lines: ")
    t2_solver.insert(END, lns_sel_pick)
    t2_solver.yview(END)

def f_lns_sel_atch_areas():
    lns_sel_atch_areas = mapdl.lsla("S")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selects those lines contained in the selected areas: ")
    t2_solver.insert(END, lns_sel_atch_areas)
    t2_solver.yview(END)

def f_lns_sel_loc():
    win_sel_loc = Toplevel()
    win_sel_loc.title("Select Lines by Location")
    win_sel_loc.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_sel_loc.winfo_screenwidth()
    h1 = win_sel_loc.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 65
    win_sel_loc.geometry('450x130+{}+{}'.format(w1, h1))
    win_sel_loc.resizable(False, False)

    def f_clear(event):
        ent_loc.delete(0, END)
        ent_loc.focus()
        var.set(0)
        
    def f_destroy(event):
        ent_loc.delete(0, END)
        win_sel_loc.destroy()
    
    def f_set_loc_OK(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.lsel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 1:
            location_y = mapdl.lsel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 2:
            location_z = mapdl.lsel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)
            win_sel_loc.destroy()
    
    def f_set_loc_apply(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.lsel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
        elif var.get() == 1:
            location_y = mapdl.lsel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
        elif var.get() == 2:
            location_z = mapdl.lsel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of lines by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)

    lab001 = Label(win_sel_loc, text = "[LSEL] Selects a subset of lines by Location")
    lab001.grid(row = 1, columnspan = 2, sticky = W, padx = 5, pady = 5)

    var = IntVar()
    var.set(0)

    loc_x = Radiobutton(win_sel_loc,
                        text = 'Location X',
                        variable = var,
                        value = 0
                        )
    loc_x.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    loc_y = Radiobutton(win_sel_loc,
                        text = 'Location Y',
                        variable = var,
                        value = 1
                        )
    loc_y.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)

    loc_z = Radiobutton(win_sel_loc,
                        text = 'Location Z',
                        variable = var,
                        value = 2
                        )
    loc_z.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    ent_loc = Entry(win_sel_loc, width = 10)
    ent_loc.grid(row = 2, column = 3, sticky = W, padx = 5, pady = 5)
    ent_loc.focus()

    btn001 = Button(win_sel_loc,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_sel_loc,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_sel_loc,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 3, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_sel_loc,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 3, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_set_loc_OK)
    btn002.bind('<Button-1>', f_set_loc_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)



def f_ars_sel_pick():
    ars_sel_pick = mapdl.asel("S", "P")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selected Areas: ")
    t2_solver.insert(END, ars_sel_pick)
    t2_solver.yview(END)

def f_ars_atch_lines():
    ars_atch_lines = mapdl.asll("S")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selects those areas containing the selected lines: ")
    t2_solver.insert(END, ars_atch_lines)
    t2_solver.yview(END)

def f_ars_atch_vol():
    ars_atch_vol = mapdl.aslv("S")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selects those areas contained in the selected volumes: ")
    t2_solver.insert(END, ars_atch_vol)
    t2_solver.yview(END)

def f_ars_sel_loc():
    win_sel_loc = Toplevel()
    win_sel_loc.title("Select Areas by Location")
    win_sel_loc.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_sel_loc.winfo_screenwidth()
    h1 = win_sel_loc.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 65
    win_sel_loc.geometry('450x130+{}+{}'.format(w1, h1))
    win_sel_loc.resizable(False, False)

    def f_clear(event):
        ent_loc.delete(0, END)
        ent_loc.focus()
        var.set(0)
        
    def f_destroy(event):
        ent_loc.delete(0, END)
        win_sel_loc.destroy()
    
    def f_set_loc_OK(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.asel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 1:
            location_y = mapdl.asel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 2:
            location_z = mapdl.asel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)
            win_sel_loc.destroy()
    
    def f_set_loc_apply(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.asel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
        elif var.get() == 1:
            location_y = mapdl.asel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
        elif var.get() == 2:
            location_z = mapdl.asel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of areas by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)

    lab001 = Label(win_sel_loc, text = "[ASEL] Selects a subset of areas by Location")
    lab001.grid(row = 1, columnspan = 2, sticky = W, padx = 5, pady = 5)

    var = IntVar()
    var.set(0)

    loc_x = Radiobutton(win_sel_loc,
                        text = 'Location X',
                        variable = var,
                        value = 0
                        )
    loc_x.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    loc_y = Radiobutton(win_sel_loc,
                        text = 'Location Y',
                        variable = var,
                        value = 1
                        )
    loc_y.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)

    loc_z = Radiobutton(win_sel_loc,
                        text = 'Location Z',
                        variable = var,
                        value = 2
                        )
    loc_z.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    ent_loc = Entry(win_sel_loc, width = 10)
    ent_loc.grid(row = 2, column = 3, sticky = W, padx = 5, pady = 5)
    ent_loc.focus()

    btn001 = Button(win_sel_loc,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_sel_loc,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_sel_loc,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 3, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_sel_loc,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 3, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_set_loc_OK)
    btn002.bind('<Button-1>', f_set_loc_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_vol_sel_pick():
    vol_sel_pick = mapdl.vsel("S", "P")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selected Picked Volumes: ")
    t2_solver.insert(END, vol_sel_pick)
    t2_solver.yview(END)

def f_vol_atch_ars():
    vol_atch_ars = mapdl.vsla("S")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Selects those volumes containing the selected areas: ")
    t2_solver.insert(END, vol_atch_ars)
    t2_solver.yview(END)

def f_vol_sel_loc():
    win_sel_loc = Toplevel()
    win_sel_loc.title("Select Volumes by Location")
    win_sel_loc.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_sel_loc.winfo_screenwidth()
    h1 = win_sel_loc.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 65
    win_sel_loc.geometry('450x130+{}+{}'.format(w1, h1))
    win_sel_loc.resizable(False, False)

    def f_clear(event):
        ent_loc.delete(0, END)
        ent_loc.focus()
        var.set(0)
        
    def f_destroy(event):
        ent_loc.delete(0, END)
        win_sel_loc.destroy()
    
    def f_set_loc_OK(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.vsel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 1:
            location_y = mapdl.vsel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
            win_sel_loc.destroy()
        elif var.get() == 2:
            location_z = mapdl.vsel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)
            win_sel_loc.destroy()
    
    def f_set_loc_apply(event):
        vmin = ent_loc.get()
        if var.get() == 0:
            location_x = mapdl.vsel("S", "LOC", "X", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location X: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_x)
            t2_solver.yview(END)
        elif var.get() == 1:
            location_y = mapdl.vsel("S", "LOC", "Y", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location Y: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_y)
            t2_solver.yview(END)
        elif var.get() == 2:
            location_z = mapdl.vsel("S", "LOC", "Z", vmin)
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Select a subset of volumes by Location Z: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, location_z)
            t2_solver.yview(END)

    lab001 = Label(win_sel_loc, text = "[VSEL] Selects a subset of volumes by Location")
    lab001.grid(row = 1, columnspan = 2, sticky = W, padx = 5, pady = 5)

    var = IntVar()
    var.set(0)

    loc_x = Radiobutton(win_sel_loc,
                        text = 'Location X',
                        variable = var,
                        value = 0
                        )
    loc_x.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    loc_y = Radiobutton(win_sel_loc,
                        text = 'Location Y',
                        variable = var,
                        value = 1
                        )
    loc_y.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)

    loc_z = Radiobutton(win_sel_loc,
                        text = 'Location Z',
                        variable = var,
                        value = 2
                        )
    loc_z.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    ent_loc = Entry(win_sel_loc, width = 10)
    ent_loc.grid(row = 2, column = 3, sticky = W, padx = 5, pady = 5)
    ent_loc.focus()

    btn001 = Button(win_sel_loc,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_sel_loc,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_sel_loc,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 3, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_sel_loc,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 3, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_set_loc_OK)
    btn002.bind('<Button-1>', f_set_loc_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_et_plane182():
    et_plane182 = mapdl.et("", "PLANE182")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Select 2D 4-Node Structural Solid: Plane182")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, et_plane182)
    t2_solver.yview(END)

def f_et_plane183():
    et_plane183 = mapdl.et("", "PLANE183")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Select 2D 8-Node or 6-Node Structural Solid: Plane183")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, et_plane183)
    t2_solver.yview(END)

def f_et_solid185():
    et_solid185 = mapdl.et("", "SOLID185")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Select 3D 8-Node Structural Solid: Solid185")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, et_solid185)
    t2_solver.yview(END)

def f_et_solid186():
    et_solid186 = mapdl.et("", "SOLID186")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Select 3D 20-Node Structural Solid: Solid186")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, et_solid186)
    t2_solver.yview(END)



def f_mat_lin_iso():
    win_mat_lin_iso = Toplevel()
    win_mat_lin_iso.title("Defines a isotripic linear material property")
    win_mat_lin_iso.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_mat_lin_iso.winfo_screenwidth()
    h1 = win_mat_lin_iso.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 160
    win_mat_lin_iso.geometry('530x320+{}+{}'.format(w1, h1))
    win_mat_lin_iso.resizable(False, False)

    def f_clear(event):
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_prxy.delete(0, END)
        ent_alpx.delete(0, END)
        ent_gxy.delete(0, END)
        ent_dens.delete(0, END)
        ent_mat.focus()
        
    def f_destroy(event):
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_prxy.delete(0, END)
        ent_alpx.delete(0, END)
        ent_gxy.delete(0, END)
        ent_dens.delete(0, END)
        win_mat_lin_iso.destroy()
    
    def f_mat_lin_iso_OK(event):
        mat = ent_mat.get()
        ex = ent_ex.get()
        prxy = ent_prxy.get()
        alpx = ent_alpx.get()
        gxy = ent_gxy.get()
        dens = ent_dens.get()
        mapdl.mp("EX", mat, ex)
        mapdl.mp("PRXY", mat, prxy)
        mapdl.mp("ALPX", mat, alpx)
        mapdl.mp("GXY", mat, gxy)
        mapdl.mp("DENS", mat, dens)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        win_mat_lin_iso.destroy()
    
    def f_mat_lin_iso_apply(event):
        mat = ent_mat.get()
        ex = ent_ex.get()
        prxy = ent_prxy.get()
        alpx = ent_alpx.get()
        gxy = ent_gxy.get()
        dens = ent_dens.get()
        mapdl.mp("EX", mat, ex)
        mapdl.mp("PRXY", mat, prxy)
        mapdl.mp("ALPX", mat, alpx)
        mapdl.mp("GXY", mat, gxy)
        mapdl.mp("DENS", mat, dens)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_prxy.delete(0, END)
        ent_alpx.delete(0, END)
        ent_gxy.delete(0, END)
        ent_dens.delete(0, END)
        ent_mat.focus()

    lab001 = Label(win_mat_lin_iso, text = "[MP] Defines a linear material property")
    lab001.grid(row = 1, columnspan = 4, sticky = W, padx = 5, pady = 5)
    
    lab002 = Label(win_mat_lin_iso, text = "MAT Material Number: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_mat = Entry(win_mat_lin_iso, width = 10)
    ent_mat.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_mat.focus()


    lab003 = Label(win_mat_lin_iso, text = "")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)
    
    lab005 = Label(win_mat_lin_iso, text = "EX Elastic Young moduli:")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_ex = Entry(win_mat_lin_iso, width = 10)
    ent_ex.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)


    lab006 = Label(win_mat_lin_iso, text = "GXY Shear moduli :")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_gxy = Entry(win_mat_lin_iso, width = 10)
    ent_gxy.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)


    lab007 = Label(win_mat_lin_iso, text = "PRXY Major Poisson's ratio:")
    lab007.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_prxy = Entry(win_mat_lin_iso, width = 10)
    ent_prxy.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)


    lab008 = Label(win_mat_lin_iso, text = "ALPX Secant coefficients of thermal expansion:")
    lab008.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 5)
    
    ent_alpx = Entry(win_mat_lin_iso, width = 10)
    ent_alpx.grid(row = 8, column = 1, sticky = W, padx = 5, pady = 5)


    lab009 = Label(win_mat_lin_iso, text = "DENS Mass density:")
    lab009.grid(row = 9, column = 0, sticky = W, padx = 5, pady = 5)

    ent_dens = Entry(win_mat_lin_iso, width = 10)
    ent_dens.grid(row = 9, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_mat_lin_iso,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_mat_lin_iso,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 15, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_mat_lin_iso,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 15, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_mat_lin_iso,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 15, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_mat_lin_iso_OK)
    btn002.bind('<Button-1>', f_mat_lin_iso_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_mat_lin_ortho():
    win_mat_lin_ortho = Toplevel()
    win_mat_lin_ortho.title("Defines a orthotropic linear material property")
    win_mat_lin_ortho.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_mat_lin_ortho.winfo_screenwidth()
    h1 = win_mat_lin_ortho.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 240
    h1 = h1 - 220
    win_mat_lin_ortho.geometry('480x440+{}+{}'.format(w1, h1))
    win_mat_lin_ortho.resizable(False, False)

    def f_clear(event):
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_ey.delete(0, END)
        ent_ez.delete(0, END)
        ent_prxy.delete(0, END)
        ent_pryz.delete(0, END)
        ent_prxz.delete(0, END)
        ent_gxy.delete(0, END)
        ent_gyz.delete(0, END)
        ent_gxz.delete(0, END)
        ent_mat.focus()
        
    def f_destroy(event):
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_ey.delete(0, END)
        ent_ez.delete(0, END)
        ent_prxy.delete(0, END)
        ent_pryz.delete(0, END)
        ent_prxz.delete(0, END)
        ent_gxy.delete(0, END)
        ent_gyz.delete(0, END)
        ent_gxz.delete(0, END)
        win_mat_lin_ortho.destroy()
    
    def f_mat_lin_ortho_OK(event):
        mat = ent_mat.get()
        ex = ent_ex.get()
        ey = ent_ey.get()
        ez = ent_ez.get()
        prxy = ent_prxy.get()
        pryz = ent_pryz.get()
        prxz = ent_prxz.get()
        gxy = ent_gxy.get()
        gyz = ent_gyz.get()
        gxz = ent_gxz.get()
        mapdl.mp("EX", mat, ex)
        mapdl.mp("EY", mat, ey)
        mapdl.mp("EZ", mat, ez)
        mapdl.mp("PRXY", mat, prxy)
        mapdl.mp("PRYZ", mat, pryz)
        mapdl.mp("PRXZ", mat, prxz)
        mapdl.mp("GXY", mat, gxy)
        mapdl.mp("GYZ", mat, gyz)
        mapdl.mp("GXZ", mat, gxz)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        win_mat_lin_ortho.destroy()
    
    def f_mat_lin_ortho_apply(event):
        mat = ent_mat.get()
        ex = ent_ex.get()
        ey = ent_ey.get()
        ez = ent_ez.get()
        prxy = ent_prxy.get()
        pryz = ent_pryz.get()
        prxz = ent_prxz.get()
        gxy = ent_gxy.get()
        gyz = ent_gyz.get()
        gxz = ent_gxz.get()
        mapdl.mp("EX", mat, ex)
        mapdl.mp("EY", mat, ey)
        mapdl.mp("EZ", mat, ez)
        mapdl.mp("PRXY", mat, prxy)
        mapdl.mp("PRYZ", mat, pryz)
        mapdl.mp("PRXZ", mat, prxz)
        mapdl.mp("GXY", mat, gxy)
        mapdl.mp("GYZ", mat, gyz)
        mapdl.mp("GXZ", mat, gxz)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        ent_mat.delete(0, END)
        ent_ex.delete(0, END)
        ent_ey.delete(0, END)
        ent_ez.delete(0, END)
        ent_prxy.delete(0, END)
        ent_pryz.delete(0, END)
        ent_prxz.delete(0, END)
        ent_gxy.delete(0, END)
        ent_gyz.delete(0, END)
        ent_gxz.delete(0, END)
        ent_mat.focus()
    
    lab001 = Label(win_mat_lin_ortho, text = "[MP] Defines a linear material property")
    lab001.grid(row = 1, columnspan = 4, sticky = W, padx = 5, pady = 5)
    
    lab002 = Label(win_mat_lin_ortho, text = "MAT Material Number: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_mat = Entry(win_mat_lin_ortho, width = 10)
    ent_mat.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_mat.focus()

    lab003 = Label(win_mat_lin_ortho, text = "")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)
    
    lab005 = Label(win_mat_lin_ortho, text = "EX Elastic Young moduli in X-Direction:")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_ex = Entry(win_mat_lin_ortho, width = 10)
    ent_ex.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_mat_lin_ortho, text = "EY Elastic Young moduli in Y-Direction:")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_ey = Entry(win_mat_lin_ortho, width = 10)
    ent_ey.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    lab007 = Label(win_mat_lin_ortho, text = "EZ Elastic Young moduli in Z-Direction:")
    lab007.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_ez = Entry(win_mat_lin_ortho, width = 10)
    ent_ez.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)

    lab008 = Label(win_mat_lin_ortho, text = "PRXY Major Poisson's ratio in XY:")
    lab008.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 5)

    ent_prxy = Entry(win_mat_lin_ortho, width = 10)
    ent_prxy.grid(row = 8, column = 1, sticky = W, padx = 5, pady = 5)

    lab009 = Label(win_mat_lin_ortho, text = "PRYZ Major Poisson's ratio in YZ:")
    lab009.grid(row = 9, column = 0, sticky = W, padx = 5, pady = 5)

    ent_pryz = Entry(win_mat_lin_ortho, width = 10)
    ent_pryz.grid(row = 9, column = 1, sticky = W, padx = 5, pady = 5)

    lab010 = Label(win_mat_lin_ortho, text = "PRXZ Major Poisson's ratio in XZ:")
    lab010.grid(row = 10, column = 0, sticky = W, padx = 5, pady = 5)

    ent_prxz = Entry(win_mat_lin_ortho, width = 10)
    ent_prxz.grid(row = 10, column = 1, sticky = W, padx = 5, pady = 5)

    lab011 = Label(win_mat_lin_ortho, text = "GXY Shear moduli in XY:")
    lab011.grid(row = 11, column = 0, sticky = W, padx = 5, pady = 5)

    ent_gxy = Entry(win_mat_lin_ortho, width = 10)
    ent_gxy.grid(row = 11, column = 1, sticky = W, padx = 5, pady = 5)

    lab012 = Label(win_mat_lin_ortho, text = "GYZ Shear moduli in YZ:")
    lab012.grid(row = 12, column = 0, sticky = W, padx = 5, pady = 5)

    ent_gyz = Entry(win_mat_lin_ortho, width = 10)
    ent_gyz.grid(row = 12, column = 1, sticky = W, padx = 5, pady = 5)

    lab013 = Label(win_mat_lin_ortho, text = "GXZ Shear moduli in XZ:")
    lab013.grid(row = 13, column = 0, sticky = W, padx = 5, pady = 5)

    ent_gxz = Entry(win_mat_lin_ortho, width = 10)
    ent_gxz.grid(row = 13, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_mat_lin_ortho,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_mat_lin_ortho,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 15, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_mat_lin_ortho,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 15, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_mat_lin_ortho,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 15, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_mat_lin_ortho_OK)
    btn002.bind('<Button-1>', f_mat_lin_ortho_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_mat_dens():
    win_mat_dens = Toplevel()
    win_mat_dens.title("Defines a density material property")
    win_mat_dens.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_mat_dens.winfo_screenwidth()
    h1 = win_mat_dens.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 95
    win_mat_dens.geometry('430x190+{}+{}'.format(w1, h1))
    win_mat_dens.resizable(False, False)

    def f_clear(event):
        ent_mat.delete(0, END)
        ent_dens.delete(0, END)
        ent_mat.focus()
        
    def f_destroy(event):
        ent_mat.delete(0, END)
        ent_dens.delete(0, END)
        win_mat_dens.destroy()
    
    def f_mat_dens_OK(event):
        mat = ent_mat.get()
        dens = ent_dens.get()
        mapdl.mp("DENS", mat, dens)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        win_mat_dens.destroy()
    
    def f_mat_dens_apply(event):
        mat = ent_mat.get()
        dens = ent_dens.get()
        mapdl.mp("DENS", mat, dens)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat)
        t2_solver.yview(END)
        ent_mat.delete(0, END)
        ent_dens.delete(0, END)
        ent_mat.focus()

    lab001 = Label(win_mat_dens, text = "[MP] Defines a density material property")
    lab001.grid(row = 1, columnspan = 4, sticky = W, padx = 5, pady = 5)
    
    lab002 = Label(win_mat_dens, text = "MAT Material Number: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_mat = Entry(win_mat_dens, width = 10)
    ent_mat.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_mat.focus()

    lab003 = Label(win_mat_dens, text = "")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_mat_dens, text = "DENS Mass density:")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_dens = Entry(win_mat_dens, width = 10)
    ent_dens.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_mat_dens,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_mat_dens,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 15, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_mat_dens,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 15, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_mat_dens,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 15, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_mat_dens_OK)
    btn002.bind('<Button-1>', f_mat_dens_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

def f_mat_del():
    win_mat_del = Toplevel()
    win_mat_del.title("Delete Material Models by Number")
    win_mat_del.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_mat_del.winfo_screenwidth()
    h1 = win_mat_del.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 225
    h1 = h1 - 95
    win_mat_del.geometry('430x190+{}+{}'.format(w1, h1))
    win_mat_del.resizable(False, False)

    def f_clear(event):
        ent_mat.delete(0, END)
        ent_lab.delete(0, END)
        ent_mat.focus()
        
    def f_destroy(event):
        ent_mat.delete(0, END)
        ent_lab.delete(0, END)
        win_mat_del.destroy()
    
    def f_mat_del_OK(event):
        mat = ent_mat.get()
        lab = ent_lab.get()
        mat_del = mapdl.mpdele(lab, mat)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model delete succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_del)
        t2_solver.yview(END)
        win_mat_del.destroy()
    
    def f_mat_del_apply(event):
        mat = ent_mat.get()
        lab = ent_lab.get()
        mat_del = mapdl.mpdele(lab, mat)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model delete succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_del)
        t2_solver.yview(END)
        ent_mat.delete(0, END)
        ent_lab.delete(0, END)
        ent_mat.focus()

    lab001 = Label(win_mat_del, text = "[MPDELE] Deletes linear material properties.")
    lab001.grid(row = 1, columnspan = 4, sticky = W, padx = 5, pady = 5)
    
    lab002 = Label(win_mat_del, text = "MAT Material Number: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_mat = Entry(win_mat_del, width = 10)
    ent_mat.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_mat.focus()

    lab003 = Label(win_mat_del, text = "")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_mat_del, text = "Lab Material Property:")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_lab = Entry(win_mat_del, width = 10)
    ent_lab.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_mat_del,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_mat_del,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 15, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_mat_del,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 15, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_mat_del,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 15, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_mat_del_OK)
    btn002.bind('<Button-1>', f_mat_del_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)
    
def f_mat_alpx():
    win_mat_alpx = Toplevel()
    win_mat_alpx.title("Thermal Expansion Secant Coeff.")
    win_mat_alpx.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_mat_alpx.winfo_screenwidth()
    h1 = win_mat_alpx.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 110
    win_mat_alpx.geometry('530x220+{}+{}'.format(w1, h1))
    win_mat_alpx.resizable(False, False)

    def f_clear(event):
        ent_mat.delete(0, END)
        ent_reft.delete(0, END)
        ent_alpx.delete(0, END)
        ent_mat.focus()
        
    def f_destroy(event):
        ent_mat.delete(0, END)
        ent_reft.delete(0, END)
        ent_alpx.delete(0, END)
        win_mat_alpx.destroy()
    
    def f_mat_alpx_OK(event):
        mat = ent_mat.get()
        reft = ent_reft.get()
        alpx = ent_alpx.get()
        mat_reft = mapdl.uimp(mat, "REFT", "", "", reft)
        mat_alpx = mapdl.mp("ALPX", mat, alpx)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model define succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_reft)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_alpx)
        t2_solver.yview(END)
        win_mat_alpx.destroy()
    
    def f_mat_alpx_apply(event):
        mat = ent_mat.get()
        reft = ent_reft.get()
        alpx = ent_alpx.get()
        mat_reft = mapdl.uimp(mat, "REFT", "", "", reft)
        mat_alpx = mapdl.mp("ALPX", mat, alpx)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model define succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_reft)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, mat_alpx)
        t2_solver.yview(END)
        ent_mat.delete(0, END)
        ent_reft.delete(0, END)
        ent_alpx.delete(0, END)
        ent_mat.focus()

    lab001 = Label(win_mat_alpx, text = "[MP] Thermal Expansion Secant Coeff.")
    lab001.grid(row = 1, columnspan = 4, sticky = W, padx = 5, pady = 5)
    
    lab002 = Label(win_mat_alpx, text = "MAT Material Number: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_mat = Entry(win_mat_alpx, width = 10)
    ent_mat.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_mat.focus()

    lab003 = Label(win_mat_alpx, text = "")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_mat_alpx, text = "REFT Reference temperature: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_reft = Entry(win_mat_alpx, width = 10)
    ent_reft.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_mat_alpx, text = "ALPX Secant coefficients of thermal expansion: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_alpx = Entry(win_mat_alpx, width = 10)
    ent_alpx.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_mat_alpx,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_mat_alpx,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 15, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_mat_alpx,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 15, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_mat_alpx,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 15, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_mat_alpx_OK)
    btn002.bind('<Button-1>', f_mat_alpx_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)



def f_wp_display():
    mapdl.plopts("WP", 1)             
    wp_displ = mapdl.wpstyl("", "", "", "", "", 0, 0, 1)
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "Work Plane is enabled:")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, wp_displ)
    t2_solver.yview(END)

def f_wp_stat():
    wp_stat = mapdl.wpstyl("STAT")
    t1_output.insert(END, "\n ")
    t1_output.insert(END, "\n ")
    t1_output.insert(END, "Work Plane status:")
    t1_output.insert(END, "\n ")
    t1_output.insert(END, wp_stat)
    t1_output.yview(END)




def f_sel_all():
    mapdl.allsel("ALL", "ALL")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "\n ")
    t2_solver.insert(END, "SELECTED ALL ENTITIES")
    t2_solver.yview(END)


def f_save_DB():
    save_DB = mapdl.save(jname, "db", "MODEL")
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END,  save_DB)
    t2_solver.yview(END)

def f_save_ALL():
    save_ALL = mapdl.save(jname, "db", "ALL")
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END,  save_ALL)
    t2_solver.yview(END)

def f_resume():
    resume_db = mapdl.resume(jname, "db")
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END, "\n" )
    t2_solver.insert(END,  resume_db)
    t2_solver.yview(END)

def f_replot():
    mapdl.replot()

# create Keypoints by Coords (K Command)
def f_kpts_coords():
    win_kpts_coords = Toplevel()
    win_kpts_coords.title("Create Keypoints by Active CSYS")
    win_kpts_coords.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_kpts_coords.winfo_screenwidth()
    h1 = win_kpts_coords.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 230
    h1 = h1 - 80
    win_kpts_coords.geometry('460x160+{}+{}'.format(w1, h1))
    win_kpts_coords.resizable(False, False)

    # clear entry
    def f_clear(event):
            ent_npt.delete(0, END)
            ent_x.delete(0, END)
            ent_y.delete(0, END)
            ent_z.delete(0, END)
            ent_npt.focus()
    
    def f_destroy(event):
            ent_npt.delete(0, END)
            ent_x.delete(0, END)
            ent_y.delete(0, END)
            ent_z.delete(0, END)
            win_kpts_coords.destroy()
    
    def f_kps_create_apply(event):
        npt_inp = ent_npt.get()
        x_inp = ent_x.get()
        y_inp = ent_y.get()
        z_inp = ent_z.get()
        kps = mapdl.k(npt_inp, x_inp, y_inp, z_inp)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create keypoint: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, kps)
        t2_solver.yview(END)
    
    def f_kps_create_OK(event):
        npt_inp = ent_npt.get()
        x_inp = ent_x.get()
        y_inp = ent_y.get()
        z_inp = ent_z.get()
        kps = mapdl.k(npt_inp, x_inp, y_inp, z_inp)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create keypoint: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, kps)
        t2_solver.yview(END)
        win_kpts_coords.destroy()
    
    
    lab001 = Label(win_kpts_coords, text = "[K] Create Keypoints in Active CSYS")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_kpts_coords, text = "NPT Keypoint number")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_kpts_coords, text = "X,Y,Z Location in active CS")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_npt = Entry(win_kpts_coords, width = 10)
    ent_npt.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)

    ent_x = Entry(win_kpts_coords, width = 10)
    ent_x.grid(row = 3, column =1, sticky = W, padx = 5, pady = 5)
    ent_x.focus()

    ent_y = Entry(win_kpts_coords, width = 10)
    ent_y.grid(row = 3, column =2, sticky = W, padx = 5, pady = 5)

    ent_z = Entry(win_kpts_coords, width = 10)
    ent_z.grid(row = 3, column =3, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_kpts_coords,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_kpts_coords,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_kpts_coords,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_kpts_coords,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_kps_create_OK)
    btn002.bind('<Button-1>', f_kps_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Lines by two Keypoints (L Command)
def f_lns_2kps():
    win_lns_l = Toplevel()
    win_lns_l.title("Create Lines by two Keypoints")
    win_lns_l.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_lns_l.winfo_screenwidth()
    h1 = win_lns_l.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 210
    h1 = h1 - 65
    win_lns_l.geometry('420x130+{}+{}'.format(w1, h1))
    win_lns_l.resizable(False, False)

    def f_clear(event):
            ent_K1.delete(0, END)
            ent_K2.delete(0, END)
            ent_K1.focus()

    
    def f_destroy(event):
            ent_K1.delete(0, END)
            ent_K2.delete(0, END)
            win_lns_l.destroy()
    
    def f_lns_create_apply(event):
        K1_inp = ent_K1.get()
        K2_inp = ent_K2.get()
        lns_2kps = mapdl.l(K1_inp, K2_inp)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, lns_2kps)
        t2_solver.yview(END)
    
    def f_lns_create_OK(event):
        K1_inp = ent_K1.get()
        K2_inp = ent_K2.get()
        lns_2kps = mapdl.l(K1_inp, K2_inp)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, lns_2kps)
        t2_solver.yview(END)
        win_lns_l.destroy()

    lab001 = Label(win_lns_l, text = "[L] Create Line by Keypoints")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_lns_l, text = "Enter keypoints numbers")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K1 = Entry(win_lns_l, width = 10)
    ent_K1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_K1.focus()

    ent_K2 = Entry(win_lns_l, width = 10)
    ent_K2.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)
    
    btn001 = Button(win_lns_l,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_lns_l,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_lns_l,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_lns_l,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_lns_create_OK)
    btn002.bind('<Button-1>', f_lns_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Areas by Keypoints (A Command)
def f_areas_by_kps():
    win_ars_a = Toplevel()
    win_ars_a.title("Define an Areas by connecting Keypoints")
    win_ars_a.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_a.winfo_screenwidth()
    h1 = win_ars_a.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 205
    win_ars_a.geometry('500x410+{}+{}'.format(w1, h1))
    win_ars_a.resizable(False, False)

    def f_clear(event):
            ent_K1.delete(0, END)
            ent_K2.delete(0, END)
            ent_K3.delete(0, END)
            ent_K4.delete(0, END)
            ent_K5.delete(0, END)
            ent_K6.delete(0, END)
            ent_K7.delete(0, END)
            ent_K8.delete(0, END)
            ent_K9.delete(0, END)
            ent_K10.delete(0, END)
            ent_K11.delete(0, END)
            ent_K12.delete(0, END)
            ent_K13.delete(0, END)
            ent_K14.delete(0, END)
            ent_K15.delete(0, END)
            ent_K16.delete(0, END)
            ent_K17.delete(0, END)
            ent_K18.delete(0, END)
            ent_K1.focus()

    
    def f_destroy(event):
            ent_K1.delete(0, END)
            ent_K2.delete(0, END)
            ent_K3.delete(0, END)
            ent_K4.delete(0, END)
            ent_K5.delete(0, END)
            ent_K6.delete(0, END)
            ent_K7.delete(0, END)
            ent_K8.delete(0, END)
            ent_K9.delete(0, END)
            ent_K10.delete(0, END)
            ent_K11.delete(0, END)
            ent_K12.delete(0, END)
            ent_K13.delete(0, END)
            ent_K14.delete(0, END)
            ent_K15.delete(0, END)
            ent_K16.delete(0, END)
            ent_K17.delete(0, END)
            ent_K18.delete(0, END)
            win_ars_a.destroy()
    
    def f_ars_a_create_apply(event):
        K1_inp = ent_K1.get()
        K2_inp = ent_K2.get()
        K3_inp = ent_K3.get()
        K4_inp = ent_K4.get()
        K5_inp = ent_K5.get()
        K6_inp = ent_K6.get()
        K7_inp = ent_K7.get()
        K8_inp = ent_K8.get()
        K9_inp = ent_K9.get()
        K10_inp = ent_K10.get()
        K11_inp = ent_K11.get()
        K12_inp = ent_K12.get()
        K13_inp = ent_K13.get()
        K14_inp = ent_K14.get()
        K15_inp = ent_K15.get()
        K16_inp = ent_K16.get()
        K17_inp = ent_K17.get()
        K18_inp = ent_K18.get()

        ars_kps = mapdl.a(K1_inp, K2_inp,
                          K3_inp, K4_inp,
                          K5_inp, K6_inp,
                          K7_inp, K8_inp,
                          K9_inp, K10_inp,
                          K11_inp, K12_inp,
                          K13_inp, K14_inp,
                          K15_inp, K16_inp,
                          K17_inp, K18_inp
                          )
        
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_kps)
        t2_solver.yview(END)
    
    def f_ars_a_create_OK(event):
        K1_inp = ent_K1.get()
        K2_inp = ent_K2.get()
        K3_inp = ent_K3.get()
        K4_inp = ent_K4.get()
        K5_inp = ent_K5.get()
        K6_inp = ent_K6.get()
        K7_inp = ent_K7.get()
        K8_inp = ent_K8.get()
        K9_inp = ent_K9.get()
        K10_inp = ent_K10.get()
        K11_inp = ent_K11.get()
        K12_inp = ent_K12.get()
        K13_inp = ent_K13.get()
        K14_inp = ent_K14.get()
        K15_inp = ent_K15.get()
        K16_inp = ent_K16.get()
        K17_inp = ent_K17.get()
        K18_inp = ent_K18.get()

        ars_kps = mapdl.a(K1_inp, K2_inp,
                          K3_inp, K4_inp,
                          K5_inp, K6_inp,
                          K7_inp, K8_inp,
                          K9_inp, K10_inp,
                          K11_inp, K12_inp,
                          K13_inp, K14_inp,
                          K15_inp, K16_inp,
                          K17_inp, K18_inp
                          )
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_kps)
        t2_solver.yview(END)
        win_ars_a.destroy()

    lab001 = Label(win_ars_a, text = "[A] Create Area by Keypoints")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_a, text = "Enter Keypoints Numbers:")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)


    lab003 = Label(win_ars_a, text = "P1, P2:")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K1 = Entry(win_ars_a, width = 10)
    ent_K1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)
    ent_K1.focus()

    ent_K2 = Entry(win_ars_a, width = 10)
    ent_K2.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)
    

    lab004 = Label(win_ars_a, text = "P3, P4:")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K3 = Entry(win_ars_a, width = 10)
    ent_K3.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K4 = Entry(win_ars_a, width = 10)
    ent_K4.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)


    lab005 = Label(win_ars_a, text = "P5, P6:")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K5 = Entry(win_ars_a, width = 10)
    ent_K5.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K6 = Entry(win_ars_a, width = 10)
    ent_K6.grid(row = 5, column = 2, sticky = W, padx = 5, pady = 5)


    lab006 = Label(win_ars_a, text = "P7, P8:")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K7 = Entry(win_ars_a, width = 10)
    ent_K7.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K8 = Entry(win_ars_a, width = 10)
    ent_K8.grid(row = 6, column = 2, sticky = W, padx = 5, pady = 5)


    lab007 = Label(win_ars_a, text = "P9, P10:")
    lab007.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K9 = Entry(win_ars_a, width = 10)
    ent_K9.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K10 = Entry(win_ars_a, width = 10)
    ent_K10.grid(row = 7, column = 2, sticky = W, padx = 5, pady = 5)


    lab008 = Label(win_ars_a, text = "P11, P12:")
    lab008.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K11 = Entry(win_ars_a, width = 10)
    ent_K11.grid(row = 8, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K12 = Entry(win_ars_a, width = 10)
    ent_K12.grid(row = 8, column = 2, sticky = W, padx = 5, pady = 5)


    lab009 = Label(win_ars_a, text = "P13, P14:")
    lab009.grid(row = 9, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K13 = Entry(win_ars_a, width = 10)
    ent_K13.grid(row = 9, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K14 = Entry(win_ars_a, width = 10)
    ent_K14.grid(row = 9, column = 2, sticky = W, padx = 5, pady = 5)


    lab010 = Label(win_ars_a, text = "P15, P16:")
    lab010.grid(row = 10, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K15 = Entry(win_ars_a, width = 10)
    ent_K15.grid(row = 10, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K16 = Entry(win_ars_a, width = 10)
    ent_K16.grid(row = 10, column = 2, sticky = W, padx = 5, pady = 5)


    lab011 = Label(win_ars_a, text = "P17, P18:")
    lab011.grid(row = 11, column = 0, sticky = W, padx = 5, pady = 5)

    ent_K17 = Entry(win_ars_a, width = 10)
    ent_K17.grid(row = 11, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_K18 = Entry(win_ars_a, width = 10)
    ent_K18.grid(row = 11, column = 2, sticky = W, padx = 5, pady = 5)


    btn001 = Button(win_ars_a,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 12, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_a,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 12, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_a,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 12, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_a,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 12, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_a_create_OK)
    btn002.bind('<Button-1>', f_ars_a_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)
    
# create Areas by Lines (AL Command)
def f_areas_by_lns():
    win_ars_al = Toplevel()
    win_ars_al.title("Generate an areas bounded by previously defined lines")
    win_ars_al.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_al.winfo_screenwidth()
    h1 = win_ars_al.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 140
    win_ars_al.geometry('500x280+{}+{}'.format(w1, h1))
    win_ars_al.resizable(False, False)

    def f_clear(event):
            ent_L1.delete(0, END)
            ent_L2.delete(0, END)
            ent_L3.delete(0, END)
            ent_L4.delete(0, END)
            ent_L5.delete(0, END)
            ent_L6.delete(0, END)
            ent_L7.delete(0, END)
            ent_L8.delete(0, END)
            ent_L9.delete(0, END)
            ent_L10.delete(0, END)
            ent_L1.focus()
    
    def f_destroy(event):
            ent_L1.delete(0, END)
            ent_L2.delete(0, END)
            ent_L3.delete(0, END)
            ent_L4.delete(0, END)
            ent_L5.delete(0, END)
            ent_L6.delete(0, END)
            ent_L7.delete(0, END)
            ent_L8.delete(0, END)
            ent_L9.delete(0, END)
            ent_L10.delete(0, END)
            win_ars_al.destroy()
    
    def f_ars_al_create_apply(event):
        L1_inp = ent_L1.get()
        L2_inp = ent_L2.get()
        L3_inp = ent_L3.get()
        L4_inp = ent_L4.get()
        L5_inp = ent_L5.get()
        L6_inp = ent_L6.get()
        L7_inp = ent_L7.get()
        L8_inp = ent_L8.get()
        L9_inp = ent_L9.get()
        L10_inp = ent_L10.get()

        ars_lns = mapdl.al(L1_inp, L2_inp,
                          L3_inp, L4_inp,
                          L5_inp, L6_inp,
                          L7_inp, L8_inp,
                          L9_inp, L10_inp,
                          )
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_lns)
        t2_solver.yview(END)
    
    def f_ars_al_create_OK(event):
        L1_inp = ent_L1.get()
        L2_inp = ent_L2.get()
        L3_inp = ent_L3.get()
        L4_inp = ent_L4.get()
        L5_inp = ent_L5.get()
        L6_inp = ent_L6.get()
        L7_inp = ent_L7.get()
        L8_inp = ent_L8.get()
        L9_inp = ent_L9.get()
        L10_inp = ent_L10.get()

        ars_lns = mapdl.al(L1_inp, L2_inp,
                          L3_inp, L4_inp,
                          L5_inp, L6_inp,
                          L7_inp, L8_inp,
                          L9_inp, L10_inp,
                          )
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_lns)
        t2_solver.yview(END)
        win_ars_al.destroy()
        

    lab001 = Label(win_ars_al, text = "[AL] Create Area by Lines")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_al, text = "Enter Lines Numbers:")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)


    lab003 = Label(win_ars_al, text = "L1, L2:")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_L1 = Entry(win_ars_al, width = 10)
    ent_L1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)
    ent_L1.focus()

    ent_L2 = Entry(win_ars_al, width = 10)
    ent_L2.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)
    

    lab004 = Label(win_ars_al, text = "L3, L4:")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_L3 = Entry(win_ars_al, width = 10)
    ent_L3.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_L4 = Entry(win_ars_al, width = 10)
    ent_L4.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)


    lab005 = Label(win_ars_al, text = "L5, L6:")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_L5 = Entry(win_ars_al, width = 10)
    ent_L5.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_L6 = Entry(win_ars_al, width = 10)
    ent_L6.grid(row = 5, column = 2, sticky = W, padx = 5, pady = 5)


    lab006 = Label(win_ars_al, text = "L7, L8:")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_L7 = Entry(win_ars_al, width = 10)
    ent_L7.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_L8 = Entry(win_ars_al, width = 10)
    ent_L8.grid(row = 6, column = 2, sticky = W, padx = 5, pady = 5)


    lab007 = Label(win_ars_al, text = "L9, L10:")
    lab007.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_L9 = Entry(win_ars_al, width = 10)
    ent_L9.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)
    
    ent_L10 = Entry(win_ars_al, width = 10)
    ent_L10.grid(row = 7, column = 2, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_ars_al,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 12, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_al,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 12, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_al,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 12, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_al,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 12, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_al_create_OK)
    btn002.bind('<Button-1>', f_ars_al_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Rectangle by 2 Corners (BLC4 Command)
def f_rect_by_2corners():
    win_ars_blc4 = Toplevel()
    win_ars_blc4.title("Create a Rectangle or Block by Corner Points")
    win_ars_blc4.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_blc4.winfo_screenwidth()
    h1 = win_ars_blc4.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 110
    win_ars_blc4.geometry('500x220+{}+{}'.format(w1, h1))
    win_ars_blc4.resizable(False, False)

    def f_clear(event):
            ent_wpx.delete(0, END)
            ent_wpy.delete(0, END)
            ent_width.delete(0, END)
            ent_height.delete(0, END)
            ent_depth.delete(0, END)
            ent_wpx.focus()
    
    def f_destroy(event):
            ent_wpx.delete(0, END)
            ent_wpy.delete(0, END)
            ent_width.delete(0, END)
            ent_height.delete(0, END)
            ent_depth.delete(0, END)
            win_ars_blc4.destroy()
    
    def f_ars_blc4_create_OK(event):
        xcorner = ent_wpx.get()
        ycorner = ent_wpy.get()
        width = ent_width.get()
        height = ent_height.get()
        depth = ent_depth.get()
        ars_blc4 = mapdl.blc4(xcorner, ycorner, width, height, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_blc4)
        t2_solver.yview(END)
        win_ars_blc4.destroy()
    
    def f_ars_blc4_create_apply(event):
        xcorner = ent_wpx.get()
        ycorner = ent_wpy.get()
        width = ent_width.get()
        height = ent_height.get()
        depth = ent_depth.get()
        ars_blc4 = mapdl.blc4(xcorner, ycorner, width, height, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_blc4)
        t2_solver.yview(END)


    lab001 = Label(win_ars_blc4, text = "[BLC4] Create Rectangle by 2 Corners")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_blc4, text = "WPX, WPY:")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_wpx = Entry(win_ars_blc4, width = 10)
    ent_wpx.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_wpx.focus()

    ent_wpy = Entry(win_ars_blc4, width = 10)
    ent_wpy.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_ars_blc4, text = "WIDTH:")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_width = Entry(win_ars_blc4, width = 10)
    ent_width.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_ars_blc4, text = "HEIGHT:")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_height = Entry(win_ars_blc4, width = 10)
    ent_height.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    label005 = Label(win_ars_blc4, text = "DEPTH:")
    label005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_depth = Entry(win_ars_blc4, width = 10)
    ent_depth.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_ars_blc4,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_blc4,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_blc4,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_blc4,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_blc4_create_OK)
    btn002.bind('<Button-1>', f_ars_blc4_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Rectangle by Center and Corners (BLC5 Command)
def f_rect_blc5():
    win_ars_blc5 = Toplevel()
    win_ars_blc5.title("Create a Rectangle or Block by Center and Corner Points")
    win_ars_blc5.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_blc5.winfo_screenwidth()
    h1 = win_ars_blc5.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 110
    win_ars_blc5.geometry('530x220+{}+{}'.format(w1, h1))
    win_ars_blc5.resizable(False, False)

    def f_clear(event):
            ent_xcenter.delete(0, END)
            ent_ycenter.delete(0, END)
            ent_width.delete(0, END)
            ent_height.delete(0, END)
            ent_depth.delete(0, END)
            ent_xcenter.focus()
    
    def f_destroy(event):
            ent_xcenter.delete(0, END)
            ent_ycenter.delete(0, END)
            ent_width.delete(0, END)
            ent_height.delete(0, END)
            ent_depth.delete(0, END)
            win_ars_blc5.destroy()
    
    def f_ars_blc5_create_OK(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        width = ent_width.get()
        height = ent_height.get()
        depth = ent_depth.get()
        ars_blc5 = mapdl.blc5(xcenter, ycenter, width, height, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_blc5)
        t2_solver.yview(END)
        win_ars_blc5.destroy()
    
    def f_ars_blc5_create_apply(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        width = ent_width.get()
        height = ent_height.get()
        depth = ent_depth.get()
        ars_blc5 = mapdl.blc5(xcenter, ycenter, width, height, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_blc5)
        t2_solver.yview(END)

    lab001 = Label(win_ars_blc5, text = "[BLC5] Create Rectangle by Center and 2 Corners")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_blc5, text = "XCENTER, YCENTER: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_xcenter = Entry(win_ars_blc5, width = 10)
    ent_xcenter.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_xcenter.focus()

    ent_ycenter = Entry(win_ars_blc5, width = 10)
    ent_ycenter.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_ars_blc5, text = "WIDTH: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_width = Entry(win_ars_blc5, width = 10)
    ent_width.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_ars_blc5, text = "HEIGHT: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_height = Entry(win_ars_blc5, width = 10)
    ent_height.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_ars_blc5, text = "DEPTH: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_depth = Entry(win_ars_blc5, width = 10)
    ent_depth.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_ars_blc5,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_blc5,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_blc5,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_blc5,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_blc5_create_OK)
    btn002.bind('<Button-1>', f_ars_blc5_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Rectangle by Dimensions (RECTNG Command)
def f_rect_rectng():
    win_ars_rectng = Toplevel()
    win_ars_rectng.title("Create Rectangle by Dimensions")
    win_ars_rectng.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_rectng.winfo_screenwidth()
    h1 = win_ars_rectng.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 80
    win_ars_rectng.geometry('500x160+{}+{}'.format(w1, h1))
    win_ars_rectng.resizable(False, False)

    def f_clear(event):
        ent_x1.delete(0, END)
        ent_x2.delete(0, END)
        ent_y1.delete(0, END)
        ent_y2.delete(0, END)
        ent_x1.focus()
    
    def f_destroy(event):
        ent_x1.delete(0, END)
        ent_x2.delete(0, END)
        ent_y1.delete(0, END)
        ent_y2.delete(0, END)
        win_ars_rectng.destroy()
    
    def f_ars_rectng_create_OK(event):
        x1 = ent_x1.get()
        x2 = ent_x2.get()
        y1 = ent_y1.get()
        y2 = ent_y2.get()
        ars_rectng = mapdl.rectng(x1, x2, y1, y2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_rectng)
        t2_solver.yview(END)
        win_ars_rectng.destroy()
    
    def f_ars_rectng_create_apply(event):
        x1 = ent_x1.get()
        x2 = ent_x2.get()
        y1 = ent_y1.get()
        y2 = ent_y2.get()
        ars_rectng = mapdl.rectng(x1, x2, y1, y2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Rectangle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_rectng)
        t2_solver.yview(END)

    lab001 = Label(win_ars_rectng, text = "[RECTNG] Create Rectangle by Dimensions")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_rectng, text = "X1, X2 X-Coordinates: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_x1 = Entry(win_ars_rectng, width = 10)
    ent_x1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_x1.focus()

    ent_x2 = Entry(win_ars_rectng, width = 10)
    ent_x2.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_ars_rectng, text = "Y1, Y2 Y-Coordinates: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_y1 = Entry(win_ars_rectng, width = 10)
    ent_y1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_y2 = Entry(win_ars_rectng, width = 10)
    ent_y2.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_ars_rectng,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_rectng,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_rectng,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_rectng,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_rectng_create_OK)
    btn002.bind('<Button-1>', f_ars_rectng_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Circle by Center and Radius (CYL4 Command)
def f_circle_cyl4():
    win_circle_cyl4 = Toplevel()
    win_circle_cyl4.title("Solid Circular Area or Cylindrical Volume")
    win_circle_cyl4.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_circle_cyl4.winfo_screenwidth()
    h1 = win_circle_cyl4.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 110
    win_circle_cyl4.geometry('500x220+{}+{}'.format(w1, h1))
    win_circle_cyl4.resizable(False, False)

    def f_clear(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        ent_xcenter.focus()
    
    def f_destroy(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        win_circle_cyl4.destroy()
    
    def f_circle_cyl4_create_OK(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        ars_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Circle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_cyl4)
        t2_solver.yview(END)
        win_circle_cyl4.destroy()
    
    def f_circle_cyl4_create_apply(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        ars_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Circle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_cyl4)
        t2_solver.yview(END)

    lab001 = Label(win_circle_cyl4, text = "[CYL4] Solid Circular Area or Cyl. Volume")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_circle_cyl4, text = "XCENTER, YCENTER: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_xcenter = Entry(win_circle_cyl4, width = 10)
    ent_xcenter.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_xcenter.focus()

    ent_ycenter = Entry(win_circle_cyl4, width = 10)
    ent_ycenter.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_circle_cyl4, text = "RAD1, THETA1: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad1 = Entry(win_circle_cyl4, width = 10)
    ent_rad1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta1 = Entry(win_circle_cyl4, width = 10)
    ent_theta1.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_circle_cyl4, text = "RAD2, THETA2: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad2 = Entry(win_circle_cyl4, width = 10)
    ent_rad2.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta2 = Entry(win_circle_cyl4, width = 10)
    ent_theta2.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_circle_cyl4, text = "DEPTH: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_depth = Entry(win_circle_cyl4, width = 10)
    ent_depth.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_circle_cyl4,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_circle_cyl4,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_circle_cyl4,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_circle_cyl4,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_circle_cyl4_create_OK)
    btn002.bind('<Button-1>', f_circle_cyl4_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Circle by Dimensions (PCIRC Command)
def f_circle_pcirc():
    win_circle_pcirc = Toplevel()
    win_circle_pcirc.title("Solid Circular Area or Cylindrical Volume")
    win_circle_pcirc.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_circle_pcirc.winfo_screenwidth()
    h1 = win_circle_pcirc.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 80
    win_circle_pcirc.geometry('500x160+{}+{}'.format(w1, h1))
    win_circle_pcirc.resizable(False, False)

    def f_clear(event):
        ent_rad1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta1.delete(0, END)
        ent_theta2.delete(0, END)
        ent_rad1.focus()
    
    def f_destroy(event):
        ent_rad1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta1.delete(0, END)
        ent_theta2.delete(0, END)
        win_circle_pcirc.destroy()
    
    def f_circle_pcirc_create_OK(event):
        rad1 = ent_rad1.get()
        rad2 = ent_rad2.get()
        theta1 = ent_theta1.get()
        theta2 = ent_theta2.get()
        ars_pcirc = mapdl.pcirc(rad1, rad2, theta1, theta2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Circle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_pcirc)
        t2_solver.yview(END)
        win_circle_pcirc.destroy()
    
    def f_circle_pcirc_create_apply(event):
        rad1 = ent_rad1.get()
        rad2 = ent_rad2.get()
        theta1 = ent_theta1.get()
        theta2 = ent_theta2.get()
        ars_pcirc = mapdl.pcirc(rad1, rad2, theta1, theta2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Circle: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_pcirc)
        t2_solver.yview(END)

    lab001 = Label(win_circle_pcirc, text = "[PCIRC] Circular Area by Dimensions")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_circle_pcirc, text = "RAD1, RAD2: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad1 = Entry(win_circle_pcirc, width = 10)
    ent_rad1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_rad1.focus()

    ent_rad2 = Entry(win_circle_pcirc, width = 10)
    ent_rad2.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_circle_pcirc, text = "THETA1, THETA2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_theta1 = Entry(win_circle_pcirc, width = 10)
    ent_theta1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta2 = Entry(win_circle_pcirc, width = 10)
    ent_theta2.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_circle_pcirc,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_circle_pcirc,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_circle_pcirc,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_circle_pcirc,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_circle_pcirc_create_OK)
    btn002.bind('<Button-1>', f_circle_pcirc_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Volumes by keypoints (V Command)
def f_vol_v():
    win_vol_v = Toplevel()
    win_vol_v.title("Defines Volumes through Keypoints")
    win_vol_v.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_v.winfo_screenwidth()
    h1 = win_vol_v.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 110
    win_vol_v.geometry('500x220+{}+{}'.format(w1, h1))
    win_vol_v.resizable(False, False)

    def f_clear(event):
        ent_p1.delete(0, END)
        ent_p2.delete(0, END)
        ent_p3.delete(0, END)
        ent_p4.delete(0, END)
        ent_p5.delete(0, END)
        ent_p6.delete(0, END)
        ent_p7.delete(0, END)
        ent_p8.delete(0, END)
        ent_p1.focus()
    
    def f_destroy(event):
        ent_p1.delete(0, END)
        ent_p2.delete(0, END)
        ent_p3.delete(0, END)
        ent_p4.delete(0, END)
        ent_p5.delete(0, END)
        ent_p6.delete(0, END)
        ent_p7.delete(0, END)
        ent_p8.delete(0, END)
        win_vol_v.destroy()
    
    def f_vol_v_create_OK(event):
        p1 = ent_p1.get()
        p2 = ent_p2.get()
        p3 = ent_p3.get()
        p4 = ent_p4.get()
        p5 = ent_p5.get()
        p6 = ent_p6.get()
        p7 = ent_p7.get()
        p8 = ent_p8.get()
        vol_v = mapdl.v(p1, p2, p3, p4, p5, p6, p7, p8)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_v)
        t2_solver.yview(END)
        win_vol_v.destroy()
    
    def f_vol_v_create_apply(event):
        p1 = ent_p1.get()
        p2 = ent_p2.get()
        p3 = ent_p3.get()
        p4 = ent_p4.get()
        p5 = ent_p5.get()
        p6 = ent_p6.get()
        p7 = ent_p7.get()
        p8 = ent_p8.get()
        vol_v = mapdl.v(p1, p2, p3, p4, p5, p6, p7, p8)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_v)
        t2_solver.yview(END)
    


    lab001 = Label(win_vol_v, text = "[V] Volume by Keypoints")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_v, text = "P1, P2: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_p1 = Entry(win_vol_v, width = 10)
    ent_p1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_p1.focus()

    ent_p2 = Entry(win_vol_v, width = 10)
    ent_p2.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_vol_v, text = "P3, P4: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_p3 = Entry(win_vol_v, width = 10)
    ent_p3.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_p4 = Entry(win_vol_v, width = 10)
    ent_p4.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_v, text = "P5, P6: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_p5 = Entry(win_vol_v, width = 10)
    ent_p5.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_p6 = Entry(win_vol_v, width = 10)
    ent_p6.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_v, text = "P7, P8: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_p7 = Entry(win_vol_v, width = 10)
    ent_p7.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    ent_p8 = Entry(win_vol_v, width = 10)
    ent_p8.grid(row = 5, column = 2, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_v,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_v,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_v,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_v,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_v_create_OK)
    btn002.bind('<Button-1>', f_vol_v_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Volumes by Areas (VA Command)
def f_vol_va():
    win_vol_va = Toplevel()
    win_vol_va.title("Generates a Volume bounded by existing Areas")
    win_vol_va.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_va.winfo_screenwidth()
    h1 = win_vol_va.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 125
    win_vol_va.geometry('500x250+{}+{}'.format(w1, h1))
    win_vol_va.resizable(False, False)

    def f_clear(event):
        ent_a1.delete(0, END)
        ent_a2.delete(0, END)
        ent_a3.delete(0, END)
        ent_a4.delete(0, END)
        ent_a5.delete(0, END)
        ent_a6.delete(0, END)
        ent_a7.delete(0, END)
        ent_a8.delete(0, END)
        ent_a9.delete(0, END)
        ent_a10.delete(0, END)
        ent_a1.focus()
    
    def f_destroy(event):
        ent_a1.delete(0, END)
        ent_a2.delete(0, END)
        ent_a3.delete(0, END)
        ent_a4.delete(0, END)
        ent_a5.delete(0, END)
        ent_a6.delete(0, END)
        ent_a7.delete(0, END)
        ent_a8.delete(0, END)
        ent_a9.delete(0, END)
        ent_a10.delete(0, END)
        win_vol_va.destroy()
    
    def f_vol_va_create_OK(event):
        a1 = ent_a1.get()
        a2 = ent_a2.get()
        a3 = ent_a3.get()
        a4 = ent_a4.get()
        a5 = ent_a5.get()
        a6 = ent_a6.get()
        a7 = ent_a7.get()
        a8 = ent_a8.get()
        a9 = ent_a9.get()
        a10 = ent_a10.get()
        vol_va = mapdl.va(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_va)
        t2_solver.yview(END)
        win_vol_va.destroy()
    
    def f_vol_va_create_apply(event):
        a1 = ent_a1.get()
        a2 = ent_a2.get()
        a3 = ent_a3.get()
        a4 = ent_a4.get()
        a5 = ent_a5.get()
        a6 = ent_a6.get()
        a7 = ent_a7.get()
        a8 = ent_a8.get()
        a9 = ent_a9.get()
        a10 = ent_a10.get()
        vol_va = mapdl.va(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_va)
        t2_solver.yview(END)

    lab001 = Label(win_vol_va, text = "[VA] Volume by Areas")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_va, text = "A1, A2: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_a1 = Entry(win_vol_va, width = 10)
    ent_a1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_a1.focus()

    ent_a2 = Entry(win_vol_va, width = 10)
    ent_a2.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_vol_va, text = "A3, A4: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_a3 = Entry(win_vol_va, width = 10)
    ent_a3.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_a4 = Entry(win_vol_va, width = 10)
    ent_a4.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_va, text = "A5, A6: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_a5 = Entry(win_vol_va, width = 10)
    ent_a5.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_a6 = Entry(win_vol_va, width = 10)
    ent_a6.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_va, text = "A7, A8: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_a7 = Entry(win_vol_va, width = 10)
    ent_a7.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    ent_a8 = Entry(win_vol_va, width = 10)
    ent_a8.grid(row = 5, column = 2, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_vol_va, text = "A9, A10: ")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_a9 = Entry(win_vol_va, width = 10)
    ent_a9.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    ent_a10 = Entry(win_vol_va, width = 10)
    ent_a10.grid(row = 6, column = 2, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_va,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_va,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 7, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_va,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 7, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_va,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 7, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_va_create_OK)
    btn002.bind('<Button-1>', f_vol_va_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# creare Solid Cylinder (CYL4 Command)
def f_vol_cyl4():
    win_vol_cyl4 = Toplevel()
    win_vol_cyl4.title("Solid Circular Area or Cylindrical Volume")
    win_vol_cyl4.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_cyl4.winfo_screenwidth()
    h1 = win_vol_cyl4.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 110
    win_vol_cyl4.geometry('500x220+{}+{}'.format(w1, h1))
    win_vol_cyl4.resizable(False, False)

    def f_clear(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        ent_xcenter.focus()
    
    def f_destroy(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        win_vol_cyl4.destroy()
    
    def f_vol_cyl4_create_OK(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        vol_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Solid Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cyl4)
        t2_solver.yview(END)
        win_vol_cyl4.destroy()
    
    def f_vol_cyl4_create_apply(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        vol_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Solid Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cyl4)
        t2_solver.yview(END)

    lab001 = Label(win_vol_cyl4, text = "[CYL4] Solid Cyl. Volume")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_cyl4, text = "XCENTER, YCENTER: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_xcenter = Entry(win_vol_cyl4, width = 10)
    ent_xcenter.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_xcenter.focus()

    ent_ycenter = Entry(win_vol_cyl4, width = 10)
    ent_ycenter.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_vol_cyl4, text = "RAD1, THETA1: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad1 = Entry(win_vol_cyl4, width = 10)
    ent_rad1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta1 = Entry(win_vol_cyl4, width = 10)
    ent_theta1.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_cyl4, text = "RAD2, THETA2: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad2 = Entry(win_vol_cyl4, width = 10)
    ent_rad2.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta2 = Entry(win_vol_cyl4, width = 10)
    ent_theta2.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_cyl4, text = "DEPTH: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_depth = Entry(win_vol_cyl4, width = 10)
    ent_depth.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_cyl4,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_cyl4,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_cyl4,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_cyl4,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_cyl4_create_OK)
    btn002.bind('<Button-1>', f_vol_cyl4_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# create Hollow Cylinder (CYL4 Command)
def f_hol_cyl4():
    win_vol_cyl4 = Toplevel()
    win_vol_cyl4.title("Create Hollow Cylinder")
    win_vol_cyl4.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_cyl4.winfo_screenwidth()
    h1 = win_vol_cyl4.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 110
    win_vol_cyl4.geometry('500x220+{}+{}'.format(w1, h1))
    win_vol_cyl4.resizable(False, False)

    def f_clear(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        ent_xcenter.focus()
    
    def f_destroy(event):
        ent_xcenter.delete(0, END)
        ent_ycenter.delete(0, END)
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_depth.delete(0, END)
        win_vol_cyl4.destroy()
    
    def f_vol_cyl4_create_OK(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        vol_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Hollow Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cyl4)
        t2_solver.yview(END)
        win_vol_cyl4.destroy()
    
    def f_vol_cyl4_create_apply(event):
        xcenter = ent_xcenter.get()
        ycenter = ent_ycenter.get()
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        depth = ent_depth.get()
        vol_cyl4 = mapdl.cyl4(xcenter, ycenter, rad1, theta1, rad2, theta2, depth)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Hollow Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cyl4)
        t2_solver.yview(END)

    lab001 = Label(win_vol_cyl4, text = "[CYL4] Hollow Cyl. Volume")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_cyl4, text = "XCENTER, YCENTER: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_xcenter = Entry(win_vol_cyl4, width = 10)
    ent_xcenter.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_xcenter.focus()

    ent_ycenter = Entry(win_vol_cyl4, width = 10)
    ent_ycenter.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 5)

    lab003 = Label(win_vol_cyl4, text = "RAD1, THETA1: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad1 = Entry(win_vol_cyl4, width = 10)
    ent_rad1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta1 = Entry(win_vol_cyl4, width = 10)
    ent_theta1.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_cyl4, text = "RAD2, THETA2: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad2 = Entry(win_vol_cyl4, width = 10)
    ent_rad2.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_theta2 = Entry(win_vol_cyl4, width = 10)
    ent_theta2.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_cyl4, text = "DEPTH: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_depth = Entry(win_vol_cyl4, width = 10)
    ent_depth.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_cyl4,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_cyl4,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 6, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_cyl4,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 6, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_cyl4,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 6, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_cyl4_create_OK)
    btn002.bind('<Button-1>', f_vol_cyl4_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)
    
# create Solid Cylinder by Dimensions (CYLIND Command)
def f_cyl_cylind():
    win_vol_cylind = Toplevel()
    win_vol_cylind.title("Create Cylinder by Dimensions")
    win_vol_cylind.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_cylind.winfo_screenwidth()
    h1 = win_vol_cylind.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 250
    h1 = h1 - 125
    win_vol_cylind.geometry('500x250+{}+{}'.format(w1, h1))
    win_vol_cylind.resizable(False, False)

    def f_clear(event):
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_z1.delete(0, END)
        ent_z2.focus()
    
    def f_destroy(event):
        ent_rad1.delete(0, END)
        ent_theta1.delete(0, END)
        ent_rad2.delete(0, END)
        ent_theta2.delete(0, END)
        ent_z1.delete(0, END)
        ent_z2.focus()
        win_vol_cylind.destroy()
    
    def f_vol_cylind_create_OK(event):
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        z1 = ent_z1.get()
        z2 = ent_z2.get()
        vol_cylind = mapdl.cylind(rad1, rad2, z1, z2, theta1, theta2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Solid Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cylind)
        t2_solver.yview(END)
        win_vol_cylind.destroy()
    
    def f_vol_cylind_create_apply(event):
        rad1 = ent_rad1.get()
        theta1 = ent_theta1.get()
        rad2 = ent_rad2.get()
        theta2 = ent_theta2.get()
        z1 = ent_z1.get()
        z2 = ent_z2.get()
        vol_cylind = mapdl.cylind(rad1, rad2, z1, z2, theta1, theta2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create Solid Cylinder: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_cylind)
        t2_solver.yview(END)

    lab001 = Label(win_vol_cylind, text = "[CYLIND] Create Cylinder by Dimensions")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_cylind, text = "RAD1 Outer radius: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad1 = Entry(win_vol_cylind, width = 10)
    ent_rad1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_rad1.focus()

    lab003 = Label(win_vol_cylind, text = "RAD2 Optional inner radius: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rad2 = Entry(win_vol_cylind, width = 10)
    ent_rad2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_cylind, text = "Z1, Z2 Z-coordinates: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_z1 = Entry(win_vol_cylind, width = 10)
    ent_z1.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_z2 = Entry(win_vol_cylind, width = 10)
    ent_z2.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_cylind, text = "THETA1 Starting angle (degrees): ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_theta1 = Entry(win_vol_cylind, width = 10)
    ent_theta1.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_vol_cylind, text = "THETA2 Ending angle (degrees): ")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_theta2 = Entry(win_vol_cylind, width = 10)
    ent_theta2.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_cylind,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_cylind,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 7, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_cylind,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 7, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_cylind,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 7, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_cylind_create_OK)
    btn002.bind('<Button-1>', f_vol_cylind_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)
    
# Boolean: add separate volumes to create a single volume (VADD Command)
def f_vol_vadd():
    win_vol_add = Toplevel()
    win_vol_add.title("Boolean operation VADD")
    win_vol_add.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_add.winfo_screenwidth()
    h1 = win_vol_add.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 190
    win_vol_add.geometry('530x380+{}+{}'.format(w1, h1))
    win_vol_add.resizable(False, False)

    def f_clear(event):
        ent_nv1.delete(0, END)
        ent_nv2.delete(0, END)
        ent_nv3.delete(0, END)
        ent_nv4.delete(0, END)
        ent_nv5.delete(0, END)
        ent_nv6.delete(0, END)
        ent_nv7.delete(0, END)
        ent_nv8.delete(0, END)
        ent_nv9.delete(0, END)
        ent_nv1.focus()
        
    
    def f_destroy(event):
        ent_nv1.delete(0, END)
        ent_nv2.delete(0, END)
        ent_nv3.delete(0, END)
        ent_nv4.delete(0, END)
        ent_nv5.delete(0, END)
        ent_nv6.delete(0, END)
        ent_nv7.delete(0, END)
        ent_nv8.delete(0, END)
        ent_nv9.delete(0, END)
        ent_nv1.focus()
        win_vol_add.destroy()
    
    def f_vol_add_create_OK(event):
        nv1 = ent_nv1.get()
        nv2 = ent_nv2.get()
        nv3 = ent_nv3.get()
        nv4 = ent_nv4.get()
        nv5 = ent_nv5.get()
        nv6 = ent_nv6.get()
        nv7 = ent_nv7.get()
        nv8 = ent_nv8.get()
        nv9 = ent_nv9.get()
        vol_vadd = mapdl.vadd(nv1, nv2, nv3, nv4, nv5, nv6, nv7, nv8, nv9)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Solid Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_vadd)
        t2_solver.yview(END)
        win_vol_add.destroy()
    
    def f_vol_add_create_apply(event):
        nv1 = ent_nv1.get()
        nv2 = ent_nv2.get()
        nv3 = ent_nv3.get()
        nv4 = ent_nv4.get()
        nv5 = ent_nv5.get()
        nv6 = ent_nv6.get()
        nv7 = ent_nv7.get()
        nv8 = ent_nv8.get()
        nv9 = ent_nv9.get()
        vol_vadd = mapdl.vadd(nv1, nv2, nv3, nv4, nv5, nv6, nv7, nv8, nv9)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Solid Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_vadd)
        t2_solver.yview(END)

    lab001 = Label(win_vol_add, text = "[VADD] Adds separate volumes into sigle volume")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_add, text = "NV1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv1 = Entry(win_vol_add, width = 10)
    ent_nv1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nv1.focus()

    lab003 = Label(win_vol_add, text = "NV2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv2 = Entry(win_vol_add, width = 10)
    ent_nv2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_add, text = "NV3: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv3 = Entry(win_vol_add, width = 10)
    ent_nv3.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_vol_add, text = "NV4: ")
    lab004.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv4 = Entry(win_vol_add, width = 10)
    ent_nv4.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_vol_add, text = "NV5: ")
    lab005.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv5 = Entry(win_vol_add, width = 10)
    ent_nv5.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_vol_add, text = "NV6: ")
    lab006.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv6 = Entry(win_vol_add, width = 10)
    ent_nv6.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)

    lab007 = Label(win_vol_add, text = "NV7: ")
    lab007.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv7 = Entry(win_vol_add, width = 10)
    ent_nv7.grid(row = 8, column = 1, sticky = W, padx = 5, pady = 5)

    lab008 = Label(win_vol_add, text = "NV8: ")
    lab008.grid(row = 9, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv8 = Entry(win_vol_add, width = 10)
    ent_nv8.grid(row = 9, column = 1, sticky = W, padx = 5, pady = 5)

    lab009 = Label(win_vol_add, text = "NV9: ")
    lab009.grid(row = 10, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv9 = Entry(win_vol_add, width = 10)
    ent_nv9.grid(row = 10, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_add,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 11, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_add,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 11, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_add,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 11, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_add,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 11, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_add_create_OK)
    btn002.bind('<Button-1>', f_vol_add_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Boolean: Adds separate areas to create a single area (AADD Command)
def f_ars_aadd():
    win_ars_aadd = Toplevel()
    win_ars_aadd.title("Boolean operation AADD")
    win_ars_aadd.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_ars_aadd.winfo_screenwidth()
    h1 = win_ars_aadd.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 190
    win_ars_aadd.geometry('530x380+{}+{}'.format(w1, h1))
    win_ars_aadd.resizable(False, False)

    def f_clear(event):
        ent_na1.delete(0, END)
        ent_na2.delete(0, END)
        ent_na3.delete(0, END)
        ent_na4.delete(0, END)
        ent_na5.delete(0, END)
        ent_na6.delete(0, END)
        ent_na7.delete(0, END)
        ent_na8.delete(0, END)
        ent_na9.delete(0, END)
        ent_na1.focus()
        
    
    def f_destroy(event):
        ent_na1.delete(0, END)
        ent_na2.delete(0, END)
        ent_na3.delete(0, END)
        ent_na4.delete(0, END)
        ent_na5.delete(0, END)
        ent_na6.delete(0, END)
        ent_na7.delete(0, END)
        ent_na8.delete(0, END)
        ent_na9.delete(0, END)
        win_ars_aadd.destroy()
    
    def f_ars_aadd_create_OK(event):
        na1 = ent_na1.get()
        na2 = ent_na2.get()
        na3 = ent_na3.get()
        na4 = ent_na4.get()
        na5 = ent_na5.get()
        na6 = ent_na6.get()
        na7 = ent_na7.get()
        na8 = ent_na8.get()
        na9 = ent_na9.get()
        ars_aadd = mapdl.aadd(na1, na2, na3, na4, na5, na6, na7, na8, na9)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_aadd)
        t2_solver.yview(END)
        win_ars_aadd.destroy()
    
    def f_ars_aadd_create_apply(event):
        na1 = ent_na1.get()
        na2 = ent_na2.get()
        na3 = ent_na3.get()
        na4 = ent_na4.get()
        na5 = ent_na5.get()
        na6 = ent_na6.get()
        na7 = ent_na7.get()
        na8 = ent_na8.get()
        na9 = ent_na9.get()
        ars_aadd = mapdl.aadd(na1, na2, na3, na4, na5, na6, na7, na8, na9)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, ars_aadd)
        t2_solver.yview(END)

    lab001 = Label(win_ars_aadd, text = "[AADD] Adds separate areas into sigle area")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_ars_aadd, text = "NA1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na1 = Entry(win_ars_aadd, width = 10)
    ent_na1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_na1.focus()

    lab003 = Label(win_ars_aadd, text = "NA2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na2 = Entry(win_ars_aadd, width = 10)
    ent_na2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_ars_aadd, text = "NA3: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na3 = Entry(win_ars_aadd, width = 10)
    ent_na3.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_ars_aadd, text = "NA4: ")
    lab004.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na4 = Entry(win_ars_aadd, width = 10)
    ent_na4.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_ars_aadd, text = "NA5: ")
    lab005.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na5 = Entry(win_ars_aadd, width = 10)
    ent_na5.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_ars_aadd, text = "NA6: ")
    lab006.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na6 = Entry(win_ars_aadd, width = 10)
    ent_na6.grid(row = 7, column = 1, sticky = W, padx = 5, pady = 5)

    lab007 = Label(win_ars_aadd, text = "NA7: ")
    lab007.grid(row = 8, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na7 = Entry(win_ars_aadd, width = 10)
    ent_na7.grid(row = 8, column = 1, sticky = W, padx = 5, pady = 5)

    lab008 = Label(win_ars_aadd, text = "NA8: ")
    lab008.grid(row = 9, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na8 = Entry(win_ars_aadd, width = 10)
    ent_na8.grid(row = 9, column = 1, sticky = W, padx = 5, pady = 5)

    lab009 = Label(win_ars_aadd, text = "NA9: ")
    lab009.grid(row = 10, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na9 = Entry(win_ars_aadd, width = 10)
    ent_na9.grid(row = 10, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_ars_aadd,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 11, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_ars_aadd,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 11, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_ars_aadd,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 11, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_ars_aadd,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 11, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_ars_aadd_create_OK)
    btn002.bind('<Button-1>', f_ars_aadd_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Boolean: Combines adjacent lines into one line (LCOMB Command)
def f_lns_lcomb():
    win_lns_lcomb = Toplevel()
    win_lns_lcomb.title("Boolean operation LCOMB")
    win_lns_lcomb.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_lns_lcomb.winfo_screenwidth()
    h1 = win_lns_lcomb.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 80
    win_lns_lcomb.geometry('530x160+{}+{}'.format(w1, h1))
    win_lns_lcomb.resizable(False, False)

    def f_clear(event):
        ent_nl1.delete(0, END)
        ent_nl2.delete(0, END)
        ent_nl1.focus()
        
    
    def f_destroy(event):
        ent_nl1.delete(0, END)
        ent_nl2.delete(0, END)
        win_lns_lcomb.destroy()
    
    def f_lns_lcomb_create_OK(event):
        nl1 = ent_nl1.get()
        nl2 = ent_nl2.get()
        lns_lcomb = mapdl.lcomb(nl1, nl2, 0)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, lns_lcomb)
        t2_solver.yview(END)
        win_lns_lcomb.destroy()
    
    def f_lns_lcomb_create_apply(event):
        nl1 = ent_nl1.get()
        nl2 = ent_nl2.get()
        lns_lcomb = mapdl.lcomb(nl1, nl2, 0)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, lns_lcomb)
        t2_solver.yview(END)

    lab001 = Label(win_lns_lcomb, text = "[LCOMB] Combines adjacent lines into one line")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_lns_lcomb, text = "NL1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl1 = Entry(win_lns_lcomb, width = 10)
    ent_nl1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nl1.focus()

    lab003 = Label(win_lns_lcomb, text = "NL2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl2 = Entry(win_lns_lcomb, width = 10)
    ent_nl2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_lns_lcomb,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_lns_lcomb,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_lns_lcomb,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_lns_lcomb,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_lns_lcomb_create_OK)
    btn002.bind('<Button-1>', f_lns_lcomb_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Boolean: Subtracts volumes from volumes (VSBV Command)
def f_vol_vsbv():
    win_vol_vsbv = Toplevel()
    win_vol_vsbv.title("Boolean operation VSBV")
    win_vol_vsbv.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_vol_vsbv.winfo_screenwidth()
    h1 = win_vol_vsbv.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 80
    win_vol_vsbv.geometry('530x160+{}+{}'.format(w1, h1))
    win_vol_vsbv.resizable(False, False)

    def f_clear(event):
        ent_nv1.delete(0, END)
        ent_nv2.delete(0, END)
        ent_nv1.focus()
        
    
    def f_destroy(event):
        ent_nv1.delete(0, END)
        ent_nv2.delete(0, END)
        win_vol_vsbv.destroy()
    
    def f_vol_vsbv_create_OK(event):
        nv1 = ent_nv1.get()
        nv2 = ent_nv2.get()
        vol_vsbv = mapdl.vsbv(nv1, nv2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_vsbv)
        t2_solver.yview(END)
        win_vol_vsbv.destroy()
    
    def f_vol_vsbv_create_apply(event):
        nv1 = ent_nv1.get()
        nv2 = ent_nv2.get()
        vol_vsbv = mapdl.vsbv(nv1, nv2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, vol_vsbv)
        t2_solver.yview(END)

    lab001 = Label(win_vol_vsbv, text = "[VSBV] Subtracts volumes from volumes")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_vol_vsbv, text = "NV1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv1 = Entry(win_vol_vsbv, width = 10)
    ent_nv1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nv1.focus()

    lab003 = Label(win_vol_vsbv, text = "NV2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nv2 = Entry(win_vol_vsbv, width = 10)
    ent_nv2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_vol_vsbv,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_vol_vsbv,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_vol_vsbv,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_vol_vsbv,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_vol_vsbv_create_OK)
    btn002.bind('<Button-1>', f_vol_vsbv_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Boolean: Subtracts areas from areas (ASBA Command)
def f_a_asba():
    win_a_asba = Toplevel()
    win_a_asba.title("Boolean operation ASBA")
    win_a_asba.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_asba.winfo_screenwidth()
    h1 = win_a_asba.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 80
    win_a_asba.geometry('530x160+{}+{}'.format(w1, h1))
    win_a_asba.resizable(False, False)

    def f_clear(event):
        ent_na1.delete(0, END)
        ent_na2.delete(0, END)
        ent_na1.focus()
        
    
    def f_destroy(event):
        ent_na1.delete(0, END)
        ent_na2.delete(0, END)
        win_a_asba.destroy()
    
    def f_a_asba_create_OK(event):
        na1 = ent_na1.get()
        na2 = ent_na2.get()
        a_asba = mapdl.asba(na1, na2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_asba)
        t2_solver.yview(END)
        win_a_asba.destroy()
    
    def f_a_asba_create_apply(event):
        na1 = ent_na1.get()
        na2 = ent_na2.get()
        a_asba = mapdl.asba(na1, na2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_asba)
        t2_solver.yview(END)

    lab001 = Label(win_a_asba, text = "[ASBA] Subtracts areas from areas")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_asba, text = "NA1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na1 = Entry(win_a_asba, width = 10)
    ent_na1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_na1.focus()

    lab003 = Label(win_a_asba, text = "NA2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na2 = Entry(win_a_asba, width = 10)
    ent_na2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_asba,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_asba,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_asba,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_asba,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_asba_create_OK)
    btn002.bind('<Button-1>', f_a_asba_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Boolean: Subtracts lines from lines (LSBL Command)
def f_l_lsbl():
    win_l_lsbl = Toplevel()
    win_l_lsbl.title("Boolean operation LSBL")
    win_l_lsbl.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_l_lsbl.winfo_screenwidth()
    h1 = win_l_lsbl.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 265
    h1 = h1 - 80
    win_l_lsbl.geometry('530x160+{}+{}'.format(w1, h1))
    win_l_lsbl.resizable(False, False)

    def f_clear(event):
        ent_nl1.delete(0, END)
        ent_nl2.delete(0, END)
        ent_nl1.focus()
        
    
    def f_destroy(event):
        ent_nl1.delete(0, END)
        ent_nl2.delete(0, END)
        win_l_lsbl.destroy()
    
    def f_l_lsbl_create_OK(event):
        nl1 = ent_nl1.get()
        nl2 = ent_nl2.get()
        l_lsbl = mapdl.lsbl(nl1, nl2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, l_lsbl)
        t2_solver.yview(END)
        win_l_lsbl.destroy()
    
    def f_l_lsbl_create_apply(event):
        nl1 = ent_nl1.get()
        nl2 = ent_nl2.get()
        l_lsbl = mapdl.lsbl(nl1, nl2)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, l_lsbl)
        t2_solver.yview(END)

    lab001 = Label(win_l_lsbl, text = "[LSBL] Subtracts lines from lines")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_l_lsbl, text = "NL1: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl1 = Entry(win_l_lsbl, width = 10)
    ent_nl1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nl1.focus()

    lab003 = Label(win_l_lsbl, text = "NL2: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl2 = Entry(win_l_lsbl, width = 10)
    ent_nl2.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_l_lsbl,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_l_lsbl,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_l_lsbl,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_l_lsbl,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_l_lsbl_create_OK)
    btn002.bind('<Button-1>', f_l_lsbl_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates a volume, offset from a given area (VOFFST Command)
def f_a_voffst():
    win_a_voffst = Toplevel()
    win_a_voffst.title("Extrude operation VOFFST")
    win_a_voffst.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_voffst.winfo_screenwidth()
    h1 = win_a_voffst.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 280
    h1 = h1 - 95
    win_a_voffst.geometry('560x190+{}+{}'.format(w1, h1))
    win_a_voffst.resizable(False, False)

    def f_clear(event):
        ent_narea.delete(0, END)
        ent_dist.delete(0, END)
        ent_narea.focus()
        
    
    def f_destroy(event):
        ent_narea.delete(0, END)
        ent_dist.delete(0, END)
        win_a_voffst.destroy()
    
    def f_a_voffst_create_OK(event):
        narea = ent_narea.get()
        dist = ent_dist.get()
        kinc = ent_kinc.get()
        a_voffst = mapdl.voffst(narea, dist, kinc)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_voffst)
        t2_solver.yview(END)
        win_a_voffst.destroy()
    
    def f_a_voffst_create_apply(event):
        narea = ent_narea.get()
        dist = ent_dist.get()
        kinc = ent_kinc.get()
        a_voffst = mapdl.voffst(narea, dist, kinc)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Line: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_voffst)
        t2_solver.yview(END)

    lab001 = Label(win_a_voffst, text = "[VOFFST] Generates a volume, offset from a given area")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_voffst, text = "NAREA Area to be extruded: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_narea = Entry(win_a_voffst, width = 10)
    ent_narea.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_narea.focus()

    lab003 = Label(win_a_voffst, text = "DIST Length of extrusion: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_dist = Entry(win_a_voffst, width = 10)
    ent_dist.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_a_voffst, text = "KINC Keypoint increment: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_kinc = Entry(win_a_voffst, width = 10)
    ent_kinc.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_voffst,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_voffst,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 5, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_voffst,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 5, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_voffst,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 5, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_voffst_create_OK)
    btn002.bind('<Button-1>', f_a_voffst_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates additional volumes by extruding areas (VEXT Command)
def f_a_vext():
    win_a_vext = Toplevel()
    win_a_vext.title("Extrude operation VEXT")
    win_a_vext.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_vext.winfo_screenwidth()
    h1 = win_a_vext.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 285
    h1 = h1 - 95
    win_a_vext.geometry('570x190+{}+{}'.format(w1, h1))
    win_a_vext.resizable(False, False)

    def f_clear(event):
        ent_na1.delete(0, END)
        ent_dx.delete(0, END)
        ent_dy.delete(0, END)
        ent_dz.delete(0, END)
        ent_rx.delete(0, END)
        ent_ry.delete(0, END)
        ent_rz.delete(0, END)
        ent_na1.focus()
        
    
    def f_destroy(event):
        ent_na1.delete(0, END)
        ent_dx.delete(0, END)
        ent_dy.delete(0, END)
        ent_dz.delete(0, END)
        ent_rx.delete(0, END)
        ent_ry.delete(0, END)
        ent_rz.delete(0, END)
        win_a_vext.destroy()
    
    def f_a_vext_create_OK(event):
        na1 = ent_na1.get()
        dx = ent_dx.get()
        dy = ent_dy.get()
        dz = ent_dz.get()
        rx = ent_rx.get()
        ry = ent_ry.get()
        rz = ent_rz.get()
        a_vext = mapdl.vext(na1, "", "", dx, dy, dz, rx, ry, rz)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vext)
        t2_solver.yview(END)
        win_a_vext.destroy()
    
    def f_a_vext_create_apply(event):
        na1 = ent_na1.get()
        dx = ent_dx.get()
        dy = ent_dy.get()
        dz = ent_dz.get()
        rx = ent_rx.get()
        ry = ent_ry.get()
        rz = ent_rz.get()
        a_vext = mapdl.vext(na1, "", "", dx, dy, dz, rx, ry, rz)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vext)
        t2_solver.yview(END)

    lab001 = Label(win_a_vext, text = "[VEXT] Generates additional volumes by extruding areas")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_vext, text = "NA1 Area to be extruded: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na1 = Entry(win_a_vext, width = 10)
    ent_na1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_na1.focus()

    lab003 = Label(win_a_vext, text = "DX, DY, DZ Offsets for extrusion: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_dx = Entry(win_a_vext, width = 10)
    ent_dx.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    ent_dy = Entry(win_a_vext, width = 10)
    ent_dy.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 5)

    ent_dz = Entry(win_a_vext, width = 10)
    ent_dz.grid(row = 3, column = 3, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_a_vext, text = "RX, RY, RZ Scale Factors: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_rx = Entry(win_a_vext, width = 10)
    ent_rx.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    ent_ry = Entry(win_a_vext, width = 10)
    ent_ry.grid(row = 4, column = 2, sticky = W, padx = 5, pady = 5)

    ent_rz = Entry(win_a_vext, width = 10)
    ent_rz.grid(row = 4, column = 3, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_vext,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_vext,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 5, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_vext,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 5, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_vext,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 5, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_vext_create_OK)
    btn002.bind('<Button-1>', f_a_vext_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates cylindrical volumes by rotating an area pattern about an axis (VROTAT Command)
def f_a_vrotat():
    win_a_vrotat = Toplevel()
    win_a_vrotat.title("Extrude operation VROTAT")
    win_a_vrotat.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_vrotat.winfo_screenwidth()
    h1 = win_a_vrotat.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 355
    h1 = h1 - 125
    win_a_vrotat.geometry('710x250+{}+{}'.format(w1, h1))
    win_a_vrotat.resizable(False, False)

    def f_clear(event):
        ent_na1.delete(0, END)
        ent_pax1.delete(0, END)
        ent_pax2.delete(0, END)
        ent_arc.delete(0, END)
        ent_nseg.delete(0, END)
        ent_na1.focus()
        
    
    def f_destroy(event):
        ent_na1.delete(0, END)
        ent_pax1.delete(0, END)
        ent_pax2.delete(0, END)
        ent_arc.delete(0, END)
        ent_nseg.delete(0, END)
        win_a_vrotat.destroy()
    
    def f_a_vrotat_create_OK(event):
        na1 = ent_na1.get()
        pax1 = ent_pax1.get()
        pax2 = ent_pax2.get()
        arc = ent_arc.get()
        nseg = ent_nseg.get()
        a_vrotat = mapdl.vrotat(na1, "", "", "", "", "", pax1, pax2, arc, nseg)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vrotat)
        t2_solver.yview(END)
        win_a_vrotat.destroy()
    
    def f_a_vrotat_create_apply(event):
        na1 = ent_na1.get()
        pax1 = ent_pax1.get()
        pax2 = ent_pax2.get()
        arc = ent_arc.get()
        nseg = ent_nseg.get()
        a_vrotat = mapdl.vrotat(na1, "", "", "", "", "", pax1, pax2, arc, nseg)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vrotat)
        t2_solver.yview(END)

    lab001 = Label(win_a_vrotat, text = "[VROTAT] Generates cylindrical volumes by rotating an area pattern about an axis")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_vrotat, text = "NA1 Area to be extruded: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na1 = Entry(win_a_vrotat, width = 10)
    ent_na1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_na1.focus()

    lab003 = Label(win_a_vrotat, text = "PAX1 Keypoint for axis: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_pax1 = Entry(win_a_vrotat, width = 10)
    ent_pax1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_a_vrotat, text = "PAX2 Keypoint for axis: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_pax2 = Entry(win_a_vrotat, width = 10)
    ent_pax2.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_a_vrotat, text = "ARC Arc length: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_arc = Entry(win_a_vrotat, width = 10)
    ent_arc.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_a_vrotat, text = "NSEG Number of volumes (8 maximum) around circumference: ")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nseg = Entry(win_a_vrotat, width = 10)
    ent_nseg.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_vrotat,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_vrotat,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 7, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_vrotat,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 7, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_vrotat,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 7, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_vrotat_create_OK)
    btn002.bind('<Button-1>', f_a_vrotat_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates volumes by dragging an area pattern along a path (VDRAG Command)
def f_a_vdrag():
    win_a_vdrag = Toplevel()
    win_a_vdrag.title("Extrude operation VDRAG")
    win_a_vdrag.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_vdrag.winfo_screenwidth()
    h1 = win_a_vdrag.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 325
    h1 = h1 - 80
    win_a_vdrag.geometry('650x160+{}+{}'.format(w1, h1))
    win_a_vdrag.resizable(False, False)

    def f_clear(event):
        ent_na1.delete(0, END)
        ent_nlp1.delete(0, END)
        ent_na1.focus()
        
    
    def f_destroy(event):
        ent_na1.delete(0, END)
        ent_nlp1.delete(0, END)
        win_a_vdrag.destroy()
    
    def f_a_vdrag_create_OK(event):
        na1 = ent_na1.get()
        nlp1 = ent_nlp1.get()
        a_vdrag = mapdl.vdrag(na1, "", "", "", "", "", nlp1, "", "", "", "", "")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vdrag)
        t2_solver.yview(END)
        win_a_vdrag.destroy()
    
    def f_a_vdrag_create_apply(event):
        na1 = ent_na1.get()
        nlp1 = ent_nlp1.get()
        a_vdrag = mapdl.vdrag(na1, "", "", "", "", "", nlp1, "", "", "", "", "")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_vdrag)
        t2_solver.yview(END)

    lab001 = Label(win_a_vdrag, text = "[VDRAG] Generates volumes by dragging an area pattern along a path")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_vdrag, text = "NA1 Area to be dragged: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_na1 = Entry(win_a_vdrag, width = 10)
    ent_na1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_na1.focus()

    lab003 = Label(win_a_vdrag, text = "NLP1 Path: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nlp1 = Entry(win_a_vdrag, width = 10)
    ent_nlp1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_vdrag,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_vdrag,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_vdrag,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_vdrag,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_vdrag_create_OK)
    btn002.bind('<Button-1>', f_a_vdrag_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates cylindrical areas by rotating a line pattern about an axis (AROTAT Command)
def f_a_arotat():
    win_a_arotat = Toplevel()
    win_a_arotat.title("Extrude operation AROTAT")
    win_a_arotat.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_arotat.winfo_screenwidth()
    h1 = win_a_arotat.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 355
    h1 = h1 - 125
    win_a_arotat.geometry('710x250+{}+{}'.format(w1, h1))
    win_a_arotat.resizable(False, False)

    def f_clear(event):
        ent_nl1.delete(0, END)
        ent_pax1.delete(0, END)
        ent_pax2.delete(0, END)
        ent_arc.delete(0, END)
        ent_nseg.delete(0, END)
        ent_nl1.focus()
        
    
    def f_destroy(event):
        ent_nl1.delete(0, END)
        ent_pax1.delete(0, END)
        ent_pax2.delete(0, END)
        ent_arc.delete(0, END)
        ent_nseg.delete(0, END)
        win_a_arotat.destroy()
    
    def f_a_arotat_create_OK(event):
        nl1 = ent_nl1.get()
        pax1 = ent_pax1.get()
        pax2 = ent_pax2.get()
        arc = ent_arc.get()
        nseg = ent_nseg.get()
        a_arotat = mapdl.arotat(nl1, "", "", "", "", "", pax1, pax2, arc, nseg)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Volume: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_arotat)
        t2_solver.yview(END)
        win_a_arotat.destroy()

    def f_a_arotat_create_apply(event):
        nl1 = ent_nl1.get()
        pax1 = ent_pax1.get()
        pax2 = ent_pax2.get()
        arc = ent_arc.get()
        nseg = ent_nseg.get()
        a_arotat = mapdl.arotat(nl1, "", "", "", "", "", pax1, pax2, arc, nseg)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_arotat)
        t2_solver.yview(END)

    lab001 = Label(win_a_arotat, text = "[AROTAT] Generates cylindrical areas by rotating a line pattern about an axis")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_arotat, text = "NL1 Line to be rotated: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl1 = Entry(win_a_arotat, width = 10)
    ent_nl1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nl1.focus()

    lab003 = Label(win_a_arotat, text = "PAX1 Keypoint for axis: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_pax1 = Entry(win_a_arotat, width = 10)
    ent_pax1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    lab004 = Label(win_a_arotat, text = "PAX2 Keypoint for axis: ")
    lab004.grid(row = 4, column = 0, sticky = W, padx = 5, pady = 5)

    ent_pax2 = Entry(win_a_arotat, width = 10)
    ent_pax2.grid(row = 4, column = 1, sticky = W, padx = 5, pady = 5)

    lab005 = Label(win_a_arotat, text = "ARC Arc length: ")
    lab005.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)

    ent_arc = Entry(win_a_arotat, width = 10)
    ent_arc.grid(row = 5, column = 1, sticky = W, padx = 5, pady = 5)

    lab006 = Label(win_a_arotat, text = "NSEG Number of areas (8 maximum) around circumference: ")
    lab006.grid(row = 6, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nseg = Entry(win_a_arotat, width = 10)
    ent_nseg.grid(row = 6, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_arotat,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_arotat,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 7, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_arotat,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 7, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_arotat,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 7, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_arotat_create_OK)
    btn002.bind('<Button-1>', f_a_arotat_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# Extrude: Generates areas by dragging a line pattern along a path (ADRAG Command)
def f_a_adrag():
    win_a_adrag = Toplevel()
    win_a_adrag.title("Extrude operation ADRAG")
    win_a_adrag.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_a_adrag.winfo_screenwidth()
    h1 = win_a_adrag.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 325
    h1 = h1 - 80
    win_a_adrag.geometry('650x160+{}+{}'.format(w1, h1))
    win_a_adrag.resizable(False, False)

    def f_clear(event):
        ent_nl1.delete(0, END)
        ent_nlp1.delete(0, END)
        ent_nl1.focus()
        
    def f_destroy(event):
        ent_nl1.delete(0, END)
        ent_nlp1.delete(0, END)
        win_a_adrag.destroy()
    
    def f_a_adrag_create_OK(event):
        nl1 = ent_nl1.get()
        nlp1 = ent_nlp1.get()
        a_adrag = mapdl.adrag(nl1, "", "", "", "", "", nlp1, "", "", "", "", "")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_adrag)
        t2_solver.yview(END)
        win_a_adrag.destroy()
    
    def f_a_adrag_create_apply(event):
        nl1 = ent_nl1.get()
        nlp1 = ent_nlp1.get()
        a_adrag = mapdl.adrag(nl1, "", "", "", "", "", nlp1, "", "", "", "", "")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create New Area: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, a_adrag)
        t2_solver.yview(END)

    lab001 = Label(win_a_adrag, text = "[ADRAG] Generates areas by dragging a line pattern along a path")
    lab001.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

    lab002 = Label(win_a_adrag, text = "NL1 Line to be dragged: ")
    lab002.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nl1 = Entry(win_a_adrag, width = 10)
    ent_nl1.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
    ent_nl1.focus()

    lab003 = Label(win_a_adrag, text = "NLP1 Path: ")
    lab003.grid(row = 3, column = 0, sticky = W, padx = 5, pady = 5)

    ent_nlp1 = Entry(win_a_adrag, width = 10)
    ent_nlp1.grid(row = 3, column = 1, sticky = W, padx = 5, pady = 5)

    btn001 = Button(win_a_adrag,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_a_adrag,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 4, column = 1, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_a_adrag,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 4, column = 2, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_a_adrag,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 4, column = 3, sticky = W, padx = 10, pady = 15)

    btn001.bind('<Button-1>', f_a_adrag_create_OK)
    btn002.bind('<Button-1>', f_a_adrag_create_apply)
    btn003.bind('<Button-1>', f_destroy)
    btn004.bind('<Button-1>', f_clear)

# clear PyMAPDL
def f_win_startPyMAPDL():
    answer = mb.askyesno("Question!", message = "You want to clear Ansys database. Are you sure?")
    if answer:
        mapdl.finish()
        mapdl.clear()
        t2_solver.delete(1.0, END)
        t1_output.delete(1.0, END)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Clear the Ansys Database: ")
        t2_solver.insert(END, "\n ")
        t2_solver.yview(END)

        enter_prep7 = mapdl.prep7()
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "ENTER THE PREPROCESSOR /PREP7: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, enter_prep7)
        t2_solver.yview(END)


def f_OneLayerPlate_fixed(event):
    win_oneL_plate = Toplevel()
    win_oneL_plate.title("1-Layer Plate (fixed support)")
    win_oneL_plate.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_oneL_plate.winfo_screenwidth()
    h1 = win_oneL_plate.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 360
    h1 = h1 - 330
    win_oneL_plate.geometry('720x660+{}+{}'.format(w1, h1))
    win_oneL_plate.resizable(False, False)

    def f_destroy(event):
        win_oneL_plate.destroy()
    
    def f_clear(event):
        ent_r.delete(0, END)
        ent_h.delete(0, END)
        ent_ex.delete(0, END)
        ent_prxy.delete(0, END)
        ent_dens.delete(0, END)
        ent_qn.delete(0, END)
        ent_q.delete(0, END)
        ent_r.focus()

    def f_create_oneL_Plate(event):
        rad1 = ent_r.get()
        depth = ent_h.get()
        mapdl.csys("1")
        l1_plate = mapdl.cyl4(0, 0, rad1, "", "", "", depth)
        cm_plate = mapdl.cm("VOLUME_PLATE", "VOLU")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create One-Layer Plate: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, l1_plate)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Create component: ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, cm_plate)
        t2_solver.yview(END)
    
    def f_plot_oneL_Plate(event):
        mapdl.vplot(vtk = True,
                 quality = 9,
                 show_volume_numbering = True,
                 show_area_numbering = False,
                 show_line_numbering = False,
                 color_areas = False,
                 show_lines = True,
                 background = "grey",
                 show_bounds = False,
                 show_axes = True,
                 cpos = "iso"
                 )
    
    def f_mat_oneL_Plate(event):
        ex = ent_ex.get()
        prxy = ent_prxy.get()
        dens = ent_dens.get()
        mapdl.mp("EX", "", ex)
        mapdl.mp("PRXY", "", prxy)
        mapdl.mp("DENS", "", dens)
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Material model ctreate succesfully: ")
        t2_solver.insert(END, "\n ")
        t2_solver.yview(END)
    
    def f_matt_list(event):
        mat_list = mapdl.mplist("ALL", "", "", "", "EVLT")
        t1_output.insert(END, "\n" )
        t1_output.insert(END, "\n" )
        t1_output.insert(END, mat_list)
        t1_output.insert(END, "\n" )
        t1_output.yview(END)
    
    uni_q = []

    def f_define_q(event):
        qnn = ent_qn.get()
        qn = int(qnn)
        q = ent_q.get()
        uni_q.append(q)
        ent_q.delete(0, END)
        if len(uni_q) == qn:
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, "Uniform Loads q define succesfully: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, uni_q)
            t2_solver.yview(END)
    

    def f_mesh_chk_ind(event):
        # Define mesh convergence parameters
        num_dof = []
        max_stress = []
        max_uz = []
        # element size: use log space since mesh converges logarithmically
        #esizes = np.linspace(0.09, 0.04, 10)
        # element size: use lin space since mesh converges linearly
        esizes = [0.08, 0.075, 0.07, 0.065, 0.06, 0.055, 0.05, 0.045, 0.04, 0.035, 0.03, 0.025, 0.02, 0.015, 0.014, 0.013, 0.012, 0.011, 0.01, 0.0095, 0.009, 0.0085, 0.008, 0.0075, 0.007, 0.0065, 0.006, 0.0055, 0.0054, 0.0053, 0.0052, 0.0051, 0.005]
        #esizes = [0.08, 0.07, 0.06]

        # run the mesh convergence and output the results on the fly
        for elem_size in esizes:
            mapdl.prep7()
            mapdl.et(1, "SOLID186")
            mapdl.type(1)
            mapdl.mat(1)
            mapdl.esys(0)

            mapdl.esize(elem_size)
            mapdl.mshape(0, "3D")
            mapdl.cmsel("S", "VOLUME_PLATE")
            mapdl.vsweep("ALL")
        
            # create components for defining loads and constraints
            mapdl.nsel("S", "LOC", "X", 0.4)                    # Select nodes on side of plate (by plate radius x = 0.4)
            cm_dof = mapdl.cm("FIXED_ALL_DOF", "NODES")         # Create nodal component FIXED_ALL_DOF
            t2_solver.insert(END, "Create component: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, cm_dof)
            t2_solver.insert(END, "\n ")
            t2_solver.yview(END)

            mapdl.nsel("S", "LOC", "Z", 0.018)                    # Select nodes on top side of plate (z = 0.018)
            cm_press = mapdl.cm("PRESSURE_DOF", "NODES")          # Create nodal component PRESSURE_DOF
            t2_solver.insert(END, "Create component: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, cm_press)
            t2_solver.insert(END, "\n ")
            t2_solver.yview(END)

            # define solution controls
            mapdl.slashsolu()              # Enter solution
            mapdl.antype("STATIC", "NEW")  # Specify a new static analysis
            mapdl.nlgeom("ON")             # Includes large-deflection effects in a static analysis or full transient
            mapdl.nsubst(10, 100, 5)       # Specifies the number of substeps to be taken this load step
            mapdl.outres("ERASE")          # Controls the solution data written to the database
            mapdl.outres("ALL", "ALL")     # Controls the solution data written to the database
            mapdl.autots("ON")             # Specifies whether to use automatic time stepping or load stepping
            mapdl.nropt("AUTO")            # Specifies the Newton-Raphson options in a static or full transient
            mapdl.eqslv("SPARSE")          # Specifies the type of equation solver
            mapdl.lumpm("OFF")             # Specifies a lumped mass matrix formulation

            # apply boundary conditions and loads
            mapdl.pbc("ALL", 1)
            mapdl.cmsel("S", "FIXED_ALL_DOF", "NODE")          # Select node component FIXED_ALL_DOF
            mapdl.d("FIXED_ALL_DOF", "ALL", 0)                 # Fix the selected nodes ALL DOF = 0
            dof_list = mapdl.dlist("ALL")                      # Lists DOF constraints
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "List of DOF Constraint: ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, dof_list)
            t1_output.yview(END)
            mapdl.allsel()


            mapdl.cmsel("S", "PRESSURE_DOF", "NODE")    # Select node component PRESSURE_DOF
            mapdl.sf("PRESSURE_DOF", "PRES", uni_q[0])  # Apply uniform pressure load to the selected node component
            mapdl.psf("PRES", "NORM", 2, 0, "ON")       # Shows surface load symbols on model displays.
            press_list = mapdl.sflist("ALL")            # Lists surface loads
            t1_output.insert(END, "List of DOF Constraint: ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, press_list)
            t1_output.yview(END)

            # solve the model
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "Begin Solution: ")
            t1_output.insert(END, "\n ")
            mapdl.allsel()
            sol_plate = mapdl.solve()
            mapdl.finish()
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, sol_plate)
            t1_output.yview(END)

            # enter post-processor
            mapdl.post1()
            mapdl.set("LAST", "LAST")

            eqv_stress = np.max(mapdl.post_processing.nodal_eqv_stress())
            uz_displ = abs(np.min(mapdl.post_processing.nodal_displacement("Z")))
        
            all_dof = mapdl.mesh.nnum_all
            dof = all_dof.size

            num_dof.append(dof)
            max_stress.append(eqv_stress)
            max_uz.append(uz_displ)
            print(f" ESIZE: {elem_size}   DOF: {dof:5d}   UZ: {uz_displ}   Stress: {eqv_stress:.2f} Pa")

            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, f" ESIZE: {elem_size}   DOF: {dof:5d}   UZ: {uz_displ}   Stress: {eqv_stress:.2f} Pa")
            t1_output.insert(END, "\n ")
            t1_output.yview(END)
            
            mapdl.prep7()
            mapdl.vclear("ALL")

        
        # Draw a dotted line showing the convergence value
        plt.plot(num_dof, max_stress, "b-o")
        plt.plot([num_dof[0], num_dof[-1]], [max_stress[-1], max_stress[-1]], "r:")
        plt.title("Mesh Convergence Study")
        plt.xlabel("Number of DOF")
        plt.ylabel("Maximum eqv. Stress (Pa)")
        plt.grid(visible = True, which = 'both', axis = 'both')
        plt.savefig('Mesh Convergence Graph')
        plt.show()

    
    def f_solve_ans(event):
        # Solve Ansys Model
        max_stress = []
        max_uz = []
        qmax = []
        opt_esize = ent_esize.get()

        # run the analysis for various q
        for q in uni_q:
            mapdl.prep7()
            mapdl.et(1, "SOLID186")
            mapdl.type(1)
            mapdl.mat(1)
            mapdl.esys(0)

            mapdl.esize(opt_esize)
            mapdl.mshape(0, "3D")
            mapdl.cmsel("S", "VOLUME_PLATE")
            mapdl.vsweep("ALL")
        
            # create components for defining loads and constraints
            mapdl.nsel("S", "LOC", "X", 0.4)                    # Select nodes on side of plate (by plate radius x = 0.4)
            cm_dof = mapdl.cm("FIXED_ALL_DOF", "NODES")         # Create nodal component FIXED_ALL_DOF
            mapdl.allsel()
            t2_solver.insert(END, "Create component: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, cm_dof)
            t2_solver.insert(END, "\n ")
            t2_solver.yview(END)

            mapdl.nsel("S", "LOC", "Z", 0.018)                    # Select nodes on top side of plate (z = 0.018)
            cm_press = mapdl.cm("PRESSURE_DOF", "NODES")          # Create nodal component PRESSURE_DOF
            mapdl.allsel()
            t2_solver.insert(END, "Create component: ")
            t2_solver.insert(END, "\n ")
            t2_solver.insert(END, cm_press)
            t2_solver.insert(END, "\n ")
            t2_solver.yview(END)

            # define solution controls
            mapdl.slashsolu()              # Enter solution
            mapdl.antype("STATIC", "NEW")  # Specify a new static analysis
            mapdl.nlgeom("ON")             # Includes large-deflection effects in a static analysis or full transient
            mapdl.nsubst(10, 100, 5)       # Specifies the number of substeps to be taken this load step
            mapdl.outres("ERASE")          # Controls the solution data written to the database
            mapdl.outres("ALL", "ALL")     # Controls the solution data written to the database
            mapdl.autots("ON")             # Specifies whether to use automatic time stepping or load stepping
            mapdl.nropt("AUTO")            # Specifies the Newton-Raphson options in a static or full transient
            mapdl.eqslv("SPARSE")          # Specifies the type of equation solver
            mapdl.lumpm("OFF")             # Specifies a lumped mass matrix formulation

            # apply boundary conditions and loads
            mapdl.pbc("ALL", 1)
            mapdl.cmsel("S", "FIXED_ALL_DOF", "NODE")          # Select node component FIXED_ALL_DOF
            mapdl.d("FIXED_ALL_DOF", "ALL", 0)                 # Fix the selected nodes ALL DOF = 0
            dof_list = mapdl.dlist("ALL")                      # Lists DOF constraints
            mapdl.allsel()
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "List of DOF Constraint: ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, dof_list)
            t1_output.yview(END)


            mapdl.cmsel("S", "PRESSURE_DOF", "NODE")    # Select node component PRESSURE_DOF
            mapdl.sf("PRESSURE_DOF", "PRES", q)         # Apply uniform pressure load to the selected node component
            mapdl.psf("PRES", "NORM", 2, 0, "ON")       # Shows surface load symbols on model displays.
            press_list = mapdl.sflist("ALL")            # Lists surface loads
            mapdl.allsel()
            t1_output.insert(END, "List of DOF Constraint: ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, press_list)
            t1_output.yview(END)

            # solve the model
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "Begin Solution: ")
            t1_output.insert(END, "\n ")
            mapdl.allsel()
            sol_plate = mapdl.solve()
            mapdl.finish()
            t1_output.insert(END, "\n ")
            t1_output.insert(END, "\n ")
            t1_output.insert(END, sol_plate)
            t1_output.yview(END)

            # enter post-processor
            mapdl.post1()
            mapdl.set("LAST", "LAST")
            
            eqv_stress = np.max(mapdl.post_processing.nodal_eqv_stress())
            uz_displ = abs(np.min(mapdl.post_processing.nodal_displacement("Z")))

            max_stress.append(eqv_stress)
            max_uz.append(uz_displ)
            qmax = uni_q 
            print(f" q: {q} Pa   UZ: {uz_displ} Meters   Stress: {eqv_stress:.2f} Pa")

            # plot Results
            sbar_kwargs = dict(title_font_size = 16,
                               label_font_size = 12,
                               shadow = True,
                               n_labels = 9,
                               italic = True,
                               bold = True,
                               fmt = "%.7f",
                               font_family = 'arial',
                               title = 'Wmax (m) - q= {q}',
                               color = 'black'
                               )
            mapdl.post_processing.plot_nodal_displacement('Z',
                                                          cpos = 'iso',
                                                          background = 'beige',
                                                          edge_color = 'black',
                                                          show_edges = True,
                                                          scalar_bar_args = sbar_kwargs,
                                                          n_colors = 256,
                                                          cmap = 'jet'
                                                          )

            
            mapdl.prep7()
            
        # draw a graph as function max_uz = f(q)
        plt.plot(qmax, max_uz, "b-o", label = "Ansys")
        plt.title("Maximum Deflection (Ansys), Wmax")
        plt.xlabel("Constant Load Intensity q, Pa")
        plt.ylabel("Maximum Deflection Wmax, meters")
        plt.grid(visible = True, which = 'both', axis = 'both')
        plt.legend()
        plt.savefig('Maximum Deflection Wmax (Ansys)')
        plt.show()

        # draw a graph as function max_stress = f(q)
        # plt.plot(qmax, max_stress, "g-o")
        # plt.title("Maximum Equivalent Stress (Ansys), Pa")
        # plt.xlabel("Constant Load Intensity q, Pa")
        # plt.ylabel("Maximum Equivalent Stress SEQV, Pa")
        # plt.grid(visible = True, which = 'both', axis = 'both')
        # plt.savefig('Maximum Equivalent Stress SEQV (Ansys)')
        # plt.show()

        return max_uz


    def f_solve_theory(event):
        # Circular Plate with uniform loading (fixed by side)
        h = float(ent_h.get())
        ex = float(ent_ex.get())
        prxy = float(ent_prxy.get())
        r = float(ent_r.get())
        
        wmax = []
        qmax = [50000, 70000, 90000, 110000]
        
        # calculate plate stiffness
        d = ex * h**3 / (12 * (1 - prxy**2))

        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, "Plate Stiffness (N/m): ")
        t2_solver.insert(END, "\n ")
        t2_solver.insert(END, d)
        t2_solver.insert(END, "\n ")
        t2_solver.yview(END)

        # calculate Wmax
        for q in qmax:
            w_max = q * r**4 / (64 * d)
            wmax.append(w_max)
        
        # print results
        print(f" q: {qmax} Pa   UZ: {wmax} Meters")

        # draw a graph as function max_uz = f(q)
        plt.plot(qmax, wmax, "r-o", label = 'Timoshenko')
        plt.title("Maximum Deflection (Timoshenko), Wmax")
        plt.xlabel("Constant Load Intensity q, Pa")
        plt.ylabel("Maximum Deflection Wmax, meters")
        plt.grid(visible = True, which = 'both', axis = 'both')
        plt.legend()
        plt.savefig('Maximum Deflection Wmax (Timoshenko)')
        plt.show()

        return wmax
    
    
    def f_sol_theory_compare(event):
        # compare results
        wmax_t = f_solve_theory(event)
        wmax_ans = f_solve_ans(event)
        qmax = uni_q
        plt.plot(qmax, wmax_ans, "b-o", label = 'Ansys')
        plt.plot(qmax, wmax_t, "r-o", label = 'Timoshenko')
        plt.title("Maximum Deflection (Compare), Wmax")
        plt.xlabel("Constant Load Intensity q, Pa")
        plt.ylabel("Maximum Deflection Wmax, meters")
        plt.grid(visible = True, which = 'both', axis = 'both')
        plt.legend()
        plt.savefig('Maximum Deflection Wmax (Compare)')
        plt.show()


    canvas1 = Canvas(win_oneL_plate,
                     width = 300,
                     height = 335,
                     background = 'white',
                     highlightbackground = 'white'
                     )
    canvas1.grid(row = 0, column = 0, rowspan = 20, sticky = NW, padx = 5, pady = 5)

    canvas1.create_image(150, 170, image = img3)
    
    label01 = Label(win_oneL_plate, text = 'Input Data for Circular Plate:')
    label01.grid(row = 0, column = 1, sticky = NW, padx = 5, pady = 5)

    label02 = Label(win_oneL_plate, text = 'R Plate radius:')
    label02.grid(row = 1, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_r = Entry(win_oneL_plate, width = 10)
    ent_r.grid(row = 1, column = 2, sticky = NW, padx = 5, pady = 5)
    ent_r.focus()

    label03 = Label(win_oneL_plate, text = 'h Plate width:')
    label03.grid(row = 2, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_h = Entry(win_oneL_plate, width = 10)
    ent_h.grid(row = 2, column = 2, sticky = NW, padx = 5, pady = 5)

    label04 = Label(win_oneL_plate, text = 'EX Elastic moduli:')
    label04.grid(row = 3, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_ex = Entry(win_oneL_plate, width = 10)
    ent_ex.grid(row = 3, column = 2, sticky = NW, padx = 5, pady = 5)

    label05 = Label(win_oneL_plate, text = 'PRXY Poisson ratio:')
    label05.grid(row = 4, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_prxy = Entry(win_oneL_plate, width = 10)
    ent_prxy.grid(row = 4, column = 2, sticky = NW, padx = 5, pady = 5)

    label06 = Label(win_oneL_plate, text = 'DENS Mass density:')
    label06.grid(row = 5, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_dens = Entry(win_oneL_plate, width = 10)
    ent_dens.grid(row = 5, column = 2, sticky = NW, padx = 5, pady = 5)

    label07 = Label(win_oneL_plate, text = 'qn Number of Loads:')
    label07.grid(row = 6, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_qn = Entry(win_oneL_plate, width = 10)
    ent_qn.grid(row = 6, column = 2, sticky = NW, padx = 5, pady = 5)

    label08 = Label(win_oneL_plate, text = 'q Uniform Load Intensity:')
    label08.grid(row = 7, column = 1, sticky = NW, padx = 5, pady = 5)

    ent_q = Entry(win_oneL_plate, width = 10)
    ent_q.grid(row = 7, column = 2, sticky = NW, padx = 5, pady = 5)


    btn000 = Button(win_oneL_plate,
                    text = "Apply",
                    width = 10,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn000.grid(row = 7, column = 3, sticky = NW, padx = 1, pady = 1)

    btn001 = Button(win_oneL_plate,
                    text = "Define Geometry",
                    width = 15,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn001.grid(row = 10, column = 1, sticky = W, padx = 10, pady = 15)

    btn002 = Button(win_oneL_plate,
                    text = "Define Material",
                    width = 15,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn002.grid(row = 10, column = 2, sticky = W, padx = 10, pady = 15)

    btn003 = Button(win_oneL_plate,
                    text = "Plot Model",
                    width = 15,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn003.grid(row = 11, column = 1, sticky = W, padx = 10, pady = 15)

    btn004 = Button(win_oneL_plate,
                    text = "List Material",
                    width = 15,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn004.grid(row = 11, column = 2, sticky = W, padx = 10, pady = 15)

    btn005 = Button(win_oneL_plate,
                    text = "Research Mesh Independency",
                    width = 25,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn005.grid(row = 12, column = 0, sticky = W, padx = 10, pady = 15)

    btn006 = Button(win_oneL_plate,
                    text = "Solve Ansys Model",
                    width = 25,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn006.grid(row = 13, column = 0, sticky = W, padx = 10, pady = 15)

    label09 = Label(win_oneL_plate, text = "Enter ESIZE:")
    label09.grid(row = 13, column = 1, sticky = W, padx = 10, pady = 15)

    ent_esize = Entry(win_oneL_plate, width = 10)
    ent_esize.grid(row = 13, column = 2, sticky = W, padx = 10, pady = 15)
    

    btn007 = Button(win_oneL_plate,
                    text = "Solve Theory Model",
                    width = 25,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn007.grid(row = 14, column = 0, sticky = W, padx = 10, pady = 15)

    btn008 = Button(win_oneL_plate,
                    text = "Compare Results",
                    width = 25,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn008.grid(row = 15, column = 0, sticky = W, padx = 10, pady = 15)

    btn009 = Button(win_oneL_plate,
                    text = "OK",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn009.grid(row = 16, column = 0, sticky = W, padx = 10, pady = 15)

    btn010 = Button(win_oneL_plate,
                    text = "Apply",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn010.grid(row = 16, column = 1, sticky = W, padx = 10, pady = 15)

    btn011 = Button(win_oneL_plate,
                    text = "Cancel",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn011.grid(row = 16, column = 2, sticky = W, padx = 10, pady = 15)

    btn012 = Button(win_oneL_plate,
                    text = "Clear",
                    width = 8,
                    height = 1,
                    borderwidth = 2,
                    overrelief = 'groove',
                    state = 'normal',
                    activebackground = 'grey',
                    activeforeground= 'white'
                    )
    btn012.grid(row = 16, column = 3, sticky = W, padx = 10, pady = 15)

    btn009.bind('<Button-1>', f_destroy)
    btn010.bind('<Button-1>', f_clear)
    btn011.bind('<Button-1>', f_destroy)
    btn012.bind('<Button-1>', f_clear)
    
    btn000.bind('<Button-1>', f_define_q)
    btn001.bind('<Button-1>', f_create_oneL_Plate)
    btn002.bind('<Button-1>', f_mat_oneL_Plate)
    btn003.bind('<Button-1>', f_plot_oneL_Plate)
    btn004.bind('<Button-1>', f_matt_list)
    btn005.bind('<Button-1>', f_mesh_chk_ind)
    btn006.bind('<Button-1>', f_solve_ans)
    btn007.bind('<Button-1>', f_solve_theory)
    btn008.bind('<Button-1>', f_sol_theory_compare)

#def f_OneLayerPlate_fixed(event):


# create New Project
def f_win_newProject():
    win_newProject = Toplevel(background = 'white')
    win_newProject.title("Define New Project...")
    win_newProject.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_newProject.winfo_screenwidth()
    h1 = win_newProject.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 300
    h1 = h1 - 200
    win_newProject.geometry('640x480+{}+{}'.format(w1, h1))
    win_newProject.resizable(False, False)

    canvas1 = Canvas(win_newProject,
                     width = 300,
                     height = 300,
                     background = 'white',
                     highlightbackground = 'white'
                     )
    canvas1.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 10)

    canvas2 = Canvas(win_newProject,
                     width = 300,
                     height = 300,
                     background = 'white',
                     highlightbackground = 'white'
                     )
    canvas2.grid(row = 1, column = 1, sticky = W, padx = 2, pady = 10)

    btn2 = Button(win_newProject,
                  text = "Select 1-Layer Plate (fixed side)",
                  width = 25,
                  height = 1,
                  borderwidth = 2,
                  overrelief = 'groove',
                  state = 'normal',
                  activebackground = 'grey',
                  activeforeground= 'white')
    btn2.grid(row = 2, column = 0, padx = 2, pady = 10)

    btn3 = Button(win_newProject,
                  text = "Select 3-Layer Plate (fixed side)",
                  width = 25,
                  height = 1,
                  borderwidth = 2,
                  overrelief = 'groove',
                  state = 'normal',
                  activebackground = 'grey',
                  activeforeground= 'white')
    btn3.grid(row = 2, column = 1, padx = 2, pady = 10)

    btn4 = Button(win_newProject,
                  text = "Select 1-Layer Plate (free support)",
                  width = 25,
                  height = 1,
                  borderwidth = 2,
                  overrelief = 'groove',
                  state = 'normal',
                  activebackground = 'grey',
                  activeforeground= 'white')
    btn4.grid(row = 3, column = 0, padx = 2, pady = 10)

    btn5 = Button(win_newProject,
                  text = "Select 3-Layer Plate (free support)",
                  width = 25,
                  height = 1,
                  borderwidth = 2,
                  overrelief = 'groove',
                  state = 'normal',
                  activebackground = 'grey',
                  activeforeground= 'white')
    btn5.grid(row = 3, column = 1, padx = 2, pady = 10)


    canvas1.create_image(152, 152, image = img1)
    canvas2.create_image(152, 152, image = img2)

    btn2.bind('<Button-1>', f_OneLayerPlate_fixed)


# open Ansys Classic GUI
def f_openAnsysGUI():
    mapdl.open_gui()
    lab1['text'] = "Ansys Classic GUI (/PREP7) is running"

# comimg soon!






# stop PyMAPDL
def f_stopPyMAPDL():
    answer = mb.askyesno("Question!", message = "You want to stop PyMAPDL. Are you sure?")
    if answer:
        t1_output.delete(1.0, END)
        t2_solver.delete(1.0, END)
        lab1['text'] = "PyMAPDL is stopped! Please exit and restart program..."
        mapdl.exit()


# about plateFEM
def f_win_about():
    win_about = Toplevel(background = 'black')
    win_about.title("About plateFEM...")
    win_about.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
    w1 = win_about.winfo_screenwidth()
    h1 = win_about.winfo_screenheight()
    w1 = w1 // 2
    h1 = h1 // 2
    w1 = w1 - 300
    h1 = h1 - 200
    win_about.geometry('640x480+{}+{}'.format(w1, h1))
    win_about.resizable(False, False)

    # functions for win_about
    def f_win_about_destroy(event):
        win_about.destroy()
    
    c2 = Canvas(win_about,
                width = 640,
                height = 430,
                background = 'black',
                highlightbackground = 'black'
                
                )
    c2.pack()
    c2.create_image(320, 215, image = img)
    
    btn1 = Button(win_about,
                  text = "OK",
                  width = 8,
                  height = 1,
                  borderwidth = 2,
                  overrelief = 'groove',
                  state = 'normal',
                  activebackground = 'grey',
                  activeforeground= 'white')
    btn1.pack()
    btn1.bind('<Button-1>', f_win_about_destroy)

# close main windpw
def f_win_destroy():
    answer = mb.askyesno("Question!", message = "You close the program. Are you sure?")
    if answer:
        t1_output.delete(1.0, END)
        t2_solver.delete(1.0, END)
        mapdl.exit()
        root.destroy()



# MAIN BLOCK
# Create main window
root = Tk()
root.title('plateFEM ' + str(__version__))
root.iconbitmap('icons\ico2_plateFEM_256x256px_color.ico')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 512                                             
h = h - 384                                           
root.geometry('1024x768+{}+{}'.format(w, h))
root.resizable(False, False)

# Define Apps Theme
ttk.Style().theme_use("classic")


# Images for children windows
img = ImageTk.PhotoImage(Image.open('images\Image_256x300px_color_about_v1.0.png'))
img1 = ImageTk.PhotoImage(Image.open('images\One-Layer Plate001_256x256.png'))
img2 = ImageTk.PhotoImage(Image.open('images\Three-Layer Plate002_256x256.png'))
img3 = ImageTk.PhotoImage(Image.open('images\One-Layer Plate003_fixed_256x256.png'))


# Create Main Menu
mainmenu = Menu(root)
root.config(menu = mainmenu)

generalmenu = Menu(mainmenu, tearoff = 0)
generalmenu.add_command(label = "Clear PyMAPDL...     Ctrl+C", command = f_win_startPyMAPDL)
generalmenu.add_command(label = "Open Ansys GUI...    Ctrl+O", command = f_openAnsysGUI)
generalmenu.add_separator()
generalmenu.add_command(label = "Resume from...         Ctrl+R", command = f_resume)
generalmenu.add_separator()
generalmenu.add_command(label = "Save db...                   Ctrl+S", command = f_save_DB)
generalmenu.add_command(label = "Save All...                   Ctrl+A", command = f_save_ALL)
generalmenu.add_separator()
generalmenu.add_command(label = "Stop PyMAPDL...      Ctrl+B", command = f_stopPyMAPDL)
generalmenu.add_separator()
generalmenu.add_command(label = "Exit...                          Ctrl+Q", command = f_win_destroy)

unitmenu = Menu(mainmenu, tearoff = 0)
unitmenu.add_command(label = "SI (kg,m,s,K,Pa,A,N,V)", command = f_sel_Units_SI)
unitmenu.add_command(label = "Metric (kg,m,s,C,A,N,V)", command = f_sel_Units_MKS)
unitmenu.add_command(label = "Metric (kg,μm,s,C,mA,N,mV)", command = f_sel_Units_uMKS)
unitmenu.add_command(label = "U.S. Customary (ft,slugs,s,F,A,lbf,PSF,V)", command = f_sel_Units_US_ft)
unitmenu.add_command(label = "U.S. Engineering (in,lbf-s²/in,s,F,A,lbf,PSI,V)", command = f_sel_Units_US_in)

select_menu = Menu(mainmenu, tearoff = 0)
select_kps_menu = Menu(select_menu, tearoff = 0)
select_kps_menu.add_command(label = "By Pick", command = f_kps_sel_pick)
select_kps_menu.add_command(label = "Attached to Lines...", command = f_kps_sel_atch_lines)
select_kps_menu.add_command(label = "Attached to Nodes...", )
select_kps_menu.add_command(label = "By Location", command = f_kps_sel_loc)

select_lines_menu = Menu(select_menu, tearoff = 0)
select_lines_menu.add_command(label = "By Pick", command = f_lns_sel_pick)
select_lines_menu.add_command(label = "Attached to Areas...", command = f_lns_sel_atch_areas)
select_lines_menu.add_command(label = "By Location", command = f_lns_sel_loc)

select_areas_menu = Menu(select_menu, tearoff = 0)
select_areas_menu.add_command(label = "By Pick", command = f_ars_sel_pick)
select_areas_menu.add_command(label = "Attached to Lines...", command = f_ars_atch_lines)
select_areas_menu.add_command(label = "Attached to Volumes...", command = f_ars_atch_vol)
select_areas_menu.add_command(label = "By Location", command = f_ars_sel_loc)

select_volumes_menu = Menu(select_menu, tearoff = 0)
select_volumes_menu.add_command(label = "By Pick", command = f_vol_sel_pick)
select_volumes_menu.add_command(label = "Attached to Areas...", command = f_vol_atch_ars)
select_volumes_menu.add_command(label = "By Location", command = f_vol_sel_loc)

select_elements_menu = Menu(select_menu, tearoff = 0)
select_elements_menu.add_command(label = "By Pick", )
select_elements_menu.add_command(label = "Attached to...", )
select_elements_menu.add_command(label = "By Attributes", )
select_elements_menu.add_command(label = "By Elem Name", )

select_nodes_menu = Menu(select_menu, tearoff = 0)
select_nodes_menu.add_command(label = "By Pick", )
select_nodes_menu.add_command(label = "Attached to...", )
select_nodes_menu.add_command(label = "By Attributes", )

components_menu = Menu(select_menu, tearoff = 0)
components_menu.add_command(label = "Volumes", )
components_menu.add_command(label = "Areas", )
components_menu.add_command(label = "Lines", )
components_menu.add_command(label = "Keypoints", )
components_menu.add_separator()
components_menu.add_command(label = "Elements", )
components_menu.add_command(label = "Nodes", )
components_menu.add_separator()
components_menu.add_command(label = "By Pick", )

plot_menu = Menu(mainmenu, tearoff = 0)
plot_menu.add_command(label = "Replot", command = f_replot)
plot_menu.add_separator()
plot_menu.add_command(label = "Keypoints", command = f_kps_plot)
plot_menu.add_command(label = "Lines", command = f_lns_plot)
plot_menu.add_command(label = "Areas", command = f_ars_plot)
plot_menu.add_command(label = "Volumes", command = f_vol_plot)
plot_menu.add_separator()
plot_menu.add_command(label = "Elements", command = f_elem_plot)
plot_menu.add_command(label = "Nodes", command = f_node_plot)
plot_menu.add_separator()
plot_menu.add_command(label = "Results", )
plot_menu.add_command(label = "Selected Components", )

plot_settings_menu = Menu(mainmenu, tearoff = 0)
plot_settings_menu.add_command(label = "Lines", )
plot_settings_menu.add_command(label = "Areas", )
plot_settings_menu.add_command(label = "Volumes", )
plot_settings_menu.add_command(label = "Elements", )
plot_settings_menu.add_command(label = "Nodes", )
plot_settings_menu.add_separator()
plot_settings_menu.add_command(label = "Results", )

work_plane_menu = Menu(mainmenu, tearoff = 0)
work_plane_menu.add_command(label = "Display Working Plane", command = f_wp_display)
work_plane_menu.add_command(label = "Show WP Status", command = f_wp_stat)
work_plane_menu.add_command(label = "WP Settings...", )
work_plane_menu.add_separator()
work_plane_menu.add_command(label = "Offset WP by Increments...", )

offset_wp_menu = Menu(work_plane_menu, tearoff = 0)
#offset_wp_menu.add_command()

align_wp_menu = Menu(work_plane_menu, tearoff = 0)
#align_wp_menu.add_command()

change_active_CS = Menu(work_plane_menu, tearoff = 0)
#change_active_CS.add_command()

change_display_CS = Menu(work_plane_menu, tearoff = 0)
#change_display_CS.add_command()

local_CS = Menu(work_plane_menu, tearoff = 0)

create_local_CS = Menu(local_CS, tearoff = 0)

list_menu = Menu(mainmenu, tearoff = 0)
list_menu.add_command(label = "Keypoints", command = f_kps_list)
list_menu.add_command(label = "Lines", command = f_lns_list)
list_menu.add_command(label = "Areas", command = f_ars_list)
list_menu.add_command(label = "Volumes", command = f_vol_list)
list_menu.add_command(label = "Elements", command = f_elem_list)
list_menu.add_command(label = "Nodes", )
list_menu.add_command(label = "Components", )
list_menu.add_separator()
list_menu.add_command(label = "Loads", )
list_menu.add_command(label = "Results", )

propmenu = Menu(list_menu, tearoff = 0)
propmenu.add_command(label = "Element Types", command = f_elem_etlist)
propmenu.add_separator()
propmenu.add_command(label = "All Materials", command = f_mat_list)

elementmenu = Menu(mainmenu, tearoff = 0)
selelementmenu = Menu(elementmenu, tearoff = 0)
selelementmenu.add_command(label = "Quad 4 node Plane 182", command = f_et_plane182)
selelementmenu.add_command(label = "Quad 8 node Plane 183", command = f_et_plane183)
selelementmenu.add_command(label = "Brick 8 node Solid 185", command = f_et_solid185)
selelementmenu.add_command(label = "Brick 20 node Solid 186", command = f_et_solid186)

keyoptsmenu = Menu(elementmenu, tearoff = 0)
keyoptsmenu.add_command(label = "KOPTS for Plane182", )
keyoptsmenu.add_command(label = "KOPTS for Plane183", )
keyoptsmenu.add_command(label = "KOPTS for Solid185", )
keyoptsmenu.add_command(label = "KOPTS for Solid186", )

matmenu = Menu(mainmenu, tearoff = 0)


alpx_menu = Menu(matmenu, tearoff = 0)
alpx_menu.add_command(label = "Isotropic", command = f_mat_alpx)
alpx_menu.add_command(label = "Orthotropic", )

operate_menu = Menu(matmenu, tearoff = 0)
operate_menu.add_command(label = "Delete Materials", command = f_mat_del)


lin_matmenu = Menu(matmenu, tearoff = 0)
lin_matmenu.add_command(label = "Isotropic", command = f_mat_lin_iso)
lin_matmenu.add_command(label = "Orthotropic", command = f_mat_lin_ortho)
#lin_matmenu.add_command(label = "Anisotropic", )


modelmenu = Menu(mainmenu, tearoff = 0)

createmenu = Menu(modelmenu, tearoff = 0)
createkeypointsmenu = Menu(createmenu, tearoff = 0)
createkeypointsmenu.add_command(label = "By Coords", command = f_kpts_coords)

createlinemenu = Menu(createmenu, tearoff = 0)
createlinemenu.add_command(label = "By Keypoints", command = f_lns_2kps)

createareasmenu = Menu(createmenu, tearoff = 0)
createareasmenu.add_command(label = "By Keypoints", command = f_areas_by_kps)
createareasmenu.add_command(label = "By Lines", command = f_areas_by_lns)

createrectanglemenu = Menu(createareasmenu, tearoff = 0)
createrectanglemenu.add_command(label = "By 2 Corners", command = f_rect_by_2corners)
createrectanglemenu.add_command(label = "By Center and Corners", command = f_rect_blc5)
createrectanglemenu.add_command(label = "By Dimensions", command = f_rect_rectng)

createcirclemenu = Menu(createareasmenu, tearoff = 0)
createcirclemenu.add_command(label = "By Center and Radius", command = f_circle_cyl4)
createcirclemenu.add_command(label = "By Dimensions", command = f_circle_pcirc)

createvolumemenu = Menu(createmenu, tearoff = 0)
arbitraryvolmenu = Menu(createvolumemenu, tearoff = 0)
arbitraryvolmenu.add_command(label = "By Keypoints", command = f_vol_v)
arbitraryvolmenu.add_command(label = "By Areas", command = f_vol_va)

cylindervolmenu = Menu(createvolumemenu, tearoff = 0)
cylindervolmenu.add_command(label = "Solid Cylinder", command = f_vol_cyl4)
cylindervolmenu.add_command(label = "Hollow Cylinder", command = f_hol_cyl4)
cylindervolmenu.add_command(label = "By Dimensions", command = f_cyl_cylind)

operatemenu = Menu(modelmenu, tearoff = 0)
extrudemenu = Menu(operatemenu, tearoff = 0)
extrudeareasmenu = Menu(extrudemenu, tearoff = 0)
extrudeareasmenu.add_command(label = "Along Normal", command = f_a_voffst)
extrudeareasmenu.add_command(label = "By XYZ Offset", command = f_a_vext)
extrudeareasmenu.add_command(label = "About Axis", command = f_a_vrotat)
extrudeareasmenu.add_command(label = "Along Lines", command = f_a_vdrag)

extrudelinesmenu = Menu(extrudemenu, tearoff = 0)
extrudelinesmenu.add_command(label = "About Axis", command = f_a_arotat)
extrudelinesmenu.add_command(label = "Along Lines", command = f_a_adrag)

boolmenu = Menu(operatemenu, tearoff = 0)
booladdmenu = Menu(boolmenu, tearoff = 0)
booladdmenu.add_command(label = "Volumes", command = f_vol_vadd)
booladdmenu.add_command(label = "Areas", command = f_ars_aadd)
booladdmenu.add_command(label = "Lines", command = f_lns_lcomb)

boolsubtractmenu = Menu(boolmenu, tearoff = 0)
boolsubtractmenu.add_command(label = "Volumes", command = f_vol_vsbv)
boolsubtractmenu.add_command(label = "Areas", command = f_a_asba)
boolsubtractmenu.add_command(label = "Lines", command = f_l_lsbl)

deletemenu = Menu(modelmenu, tearoff = 0)
deletemenu.add_command(label = "Keypoints", command = f_kps_del_all)
deletemenu.add_command(label = "Lines", command = f_lns_del_all)
deletemenu.add_command(label = "Areas", command = f_ars_del_all)
deletemenu.add_command(label = "Volumes", command = f_vol_del_all)

platewizard = Menu(modelmenu, tearoff = 0)
platewizard.add_command(label = "Plate Wizard", command = f_win_newProject)

meshmenu = Menu(mainmenu, tearoff = 0)
meshattrmenu = Menu(meshmenu, tearoff = 0)
meshattrmenu.add_command(label = "All Keypoints", )
meshattrmenu.add_command(label = "All Lines", )
meshattrmenu.add_command(label = "All Areas", )
meshattrmenu.add_command(label = "All Volumes", )

meshsizemenu = Menu(meshmenu, tearoff = 0)
meshsizemenu.add_command(label = "SmartSize", )
meshsizemenu.add_command(label = "Global Mesh Size", )
meshsizemenu.add_command(label = "Areas Mesh Size", )
meshsizemenu.add_command(label = "Lines Mesh Size", )

genmeshmenu = Menu(meshmenu, tearoff = 0)
genmeshmenu.add_command(label = "Generate Volume Mesh", )
genmeshmenu.add_command(label = "Generate Area Mesh", )

loads_menu = Menu(mainmenu, tearoff = 0)
define_loads_menu = Menu(loads_menu, tearoff = 0)
displ_loads_menu = Menu(define_loads_menu, tearoff = 0)
displ_loads_menu.add_command(label = "On Lines", )
displ_loads_menu.add_command(label = "On Areas", )
displ_loads_menu.add_command(label = "On Nodes", )
displ_loads_menu.add_command(label = "On Node Components", )

force_loads_menu = Menu(define_loads_menu, tearoff = 0)
force_loads_menu.add_command(label = "On Keypoints", )
force_loads_menu.add_command(label = "On Nodes", )
force_loads_menu.add_command(label = "On Node Components", )

pressure_loads_menu = Menu(define_loads_menu, tearoff = 0)
pressure_loads_menu.add_command(label = "On Lines", )
pressure_loads_menu.add_command(label = "On Areas", )
pressure_loads_menu.add_command(label = "On Nodes", )
pressure_loads_menu.add_command(label = "On Node Components", )
pressure_loads_menu.add_command(label = "On Elements", )
pressure_loads_menu.add_command(label = "On Element Components", )

delete_loads_menu = Menu(loads_menu, tearoff = 0)
delete_displ_loads_menu = Menu(delete_loads_menu, tearoff = 0)
delete_displ_loads_menu.add_command(label = "On Lines", )
delete_displ_loads_menu.add_command(label = "On Areas", )
delete_displ_loads_menu.add_command(label = "On Nodes", )
delete_displ_loads_menu.add_command(label = "On Node Components", )

delete_force_loads_menu = Menu(delete_loads_menu, tearoff = 0)
delete_force_loads_menu.add_command(label = "On Keypoints", )
delete_force_loads_menu.add_command(label = "On Nodes", )
delete_force_loads_menu.add_command(label = "On Node Components", )

delete_pressure_loads_menu = Menu(delete_loads_menu, tearoff = 0)
delete_pressure_loads_menu.add_command(label = "On Lines", )
delete_pressure_loads_menu.add_command(label = "On Areas", )
delete_pressure_loads_menu.add_command(label = "On Nodes", )
delete_pressure_loads_menu.add_command(label = "On Node Components", )
delete_pressure_loads_menu.add_command(label = "On Elements", )
delete_pressure_loads_menu.add_command(label = "On Element Components", )

delete_all_load_data_menu = Menu(delete_loads_menu, tearoff = 0)
delete_all_load_data_menu.add_command(label = "All Loads and Opts", )
delete_all_load_data_menu.add_command(label = "All Solid Mod Loads", )
delete_all_load_data_menu.add_command(label = "All FE Loads", )

operate_loads_menu = Menu(loads_menu, tearoff = 0)
operate_loads_menu.add_command(label = "Transfer All Solid to FE", )
#operate_loads_menu.add_command(label = "", )
#operate_loads_menu.add_command(label = "", )
#operate_loads_menu.add_command(label = "", )

solution_menu = Menu(mainmenu, tearoff = 0)
antype_menu = Menu(solution_menu, tearoff = 0)
antype_menu.add_command(label = "New Analysis", )
antype_menu.add_command(label = "Solution Controls", )

solve_type_menu = Menu(solution_menu, tearoff = 0)
solve_type_menu.add_command(label = "Run Solution", )

res_menu = Menu(mainmenu, tearoff = 0)
read_menu = Menu(res_menu, tearoff = 0)
read_menu.add_command(label = "First Set", )
read_menu.add_command(label = "Next Set", )
read_menu.add_command(label = "Last Set", )
read_menu.add_command(label = "By Pick", )

plot_res_menu = Menu(res_menu, tearoff = 0)
plot_res_menu.add_command(label = "Deformed Shape", )
plot_res_menu.add_command(label = "Nodal Solu", )
plot_res_menu.add_command(label = "Element Solu", )

list_res_menu = Menu(res_menu, tearoff = 0)
list_res_menu.add_command(label = "Nodal Solu", )
list_res_menu.add_command(label = "Element Solu", )

helpmenu = Menu(mainmenu, tearoff = 0)
helpmenu.add_command(label = "Ansys MAPDL Help", )
helpmenu.add_separator()
helpmenu.add_command(label = "Ansys MAPDL Command Reference", )
helpmenu.add_command(label = "Ansys MAPDL Element Reference", )
helpmenu.add_separator()
helpmenu.add_command(label = "Ansys PyMAPDL Docs", )
helpmenu.add_command(label = "Ansys Python Docs", )
helpmenu.add_separator()
helpmenu.add_command(label = "Getting Started PyAnsys", )
helpmenu.add_command(label = "Getting Started PyMAPDL", )
helpmenu.add_separator()
helpmenu.add_command(label = "About plateFEM...", command = f_win_about)


# ***MAIN MENU ENTITIES***
mainmenu.add_cascade(label = "Main Menu", menu = generalmenu)
mainmenu.add_cascade(label = "Units", menu = unitmenu)
mainmenu.add_cascade(label = "Select", menu = select_menu)
mainmenu.add_cascade(label = "List", menu = list_menu)
mainmenu.add_cascade(label = "Plot", menu = plot_menu)
mainmenu.add_cascade(label = "PlotCtrls", menu = plot_settings_menu)
mainmenu.add_cascade(label = "WorkPlane", menu = work_plane_menu)
mainmenu.add_cascade(label = "Element Library", menu = elementmenu)
mainmenu.add_cascade(label = "Material Models", menu = matmenu)
mainmenu.add_cascade(label = "Modeling", menu = modelmenu)
mainmenu.add_cascade(label = "Meshing", menu = meshmenu)
mainmenu.add_cascade(label = "Loads", menu = loads_menu)
mainmenu.add_cascade(label = "Solution", menu = solution_menu)
mainmenu.add_cascade(label = "Postprocessor", menu = res_menu)
mainmenu.add_cascade(label = "Help", menu = helpmenu)


modelmenu.add_cascade(label = "Create", menu = createmenu)
modelmenu.add_cascade(label = "Operate", menu = operatemenu)
modelmenu.add_cascade(label = "Delete", menu = deletemenu)
modelmenu.add_cascade(label = "Circular Plate", menu = platewizard)
elementmenu.add_cascade(label = "Select Element", menu = selelementmenu)
elementmenu.add_cascade(label = "Element Operations", menu = keyoptsmenu)
meshmenu.add_cascade(label = "Define Mesh Attributes", menu = meshattrmenu)
meshmenu.add_cascade(label = "Define Mesh Size", menu = meshsizemenu)
meshmenu.add_cascade(label = "Generate Mesh", menu = genmeshmenu)
createmenu.add_cascade(label = "Keypoints", menu = createkeypointsmenu)
createmenu.add_cascade(label = "Lines", menu = createlinemenu)
createmenu.add_cascade(label = "Areas", menu = createareasmenu)
createmenu.add_cascade(label = "Volumes", menu = createvolumemenu)
createareasmenu.add_cascade(label = "Rectangle", menu = createrectanglemenu)
createareasmenu.add_cascade(label = "Circle", menu = createcirclemenu)
createvolumemenu.add_cascade(label = "Arbitrary", menu = arbitraryvolmenu)
createvolumemenu.add_cascade(label = "Cylinder", menu = cylindervolmenu)
operatemenu.add_cascade(label = "Booleans", menu = boolmenu)
boolmenu.add_cascade(label = "Add", menu = booladdmenu)
boolmenu.add_cascade(label = "Subtract", menu = boolsubtractmenu)
operatemenu.add_cascade(label = "Extrude", menu = extrudemenu)
extrudemenu.add_cascade(label = "Areas", menu = extrudeareasmenu)
extrudemenu.add_cascade(label = "Lines", menu = extrudelinesmenu)
loads_menu.add_cascade(label = "Define", menu = define_loads_menu)
loads_menu.add_cascade(label = "Delete", menu = delete_loads_menu)
loads_menu.add_cascade(label = "Operate", menu = operate_loads_menu)
delete_loads_menu.add_cascade(label = "Displacement", menu = delete_displ_loads_menu)
delete_loads_menu.add_cascade(label = "Force/Moments", menu = delete_force_loads_menu)
delete_loads_menu.add_cascade(label = "Pressure", menu = delete_pressure_loads_menu)
delete_loads_menu.add_cascade(label = "All Load Data", menu = delete_all_load_data_menu)
define_loads_menu.add_cascade(label = "Displacement", menu = displ_loads_menu)
define_loads_menu.add_cascade(label = "Force/Moments", menu = force_loads_menu)
define_loads_menu.add_cascade(label = "Pressure", menu = pressure_loads_menu)
select_menu.add_cascade(label = "Keypoints", menu = select_kps_menu)
select_menu.add_cascade(label = "Lines", menu = select_lines_menu)
select_menu.add_cascade(label = "Areas", menu = select_areas_menu)
select_menu.add_cascade(label = "Volumes", menu = select_volumes_menu)
select_menu.add_cascade(label = "Elements", menu = select_elements_menu)
select_menu.add_cascade(label = "Nodes", menu = select_nodes_menu)
select_menu.add_separator()
select_menu.add_cascade(label = "Create Components", menu = components_menu)
select_menu.add_separator()
select_menu.add_command(label = "Select Everything", command = f_sel_all)
solution_menu.add_cascade(label = "Analysis Type", menu = antype_menu)
solution_menu.add_cascade(label = "Solve", menu = solve_type_menu)
res_menu.add_cascade(label = "Read Results", menu = read_menu)
res_menu.add_cascade(label = "Plot Results", menu = plot_res_menu)
res_menu.add_cascade(label = "List Results", menu = list_res_menu)
list_menu.add_cascade(label = "Properties", menu = propmenu)
matmenu.add_cascade(label = "Linear Elastic", menu = lin_matmenu)
matmenu.add_cascade(label = "Thermal Expansion Coeff.", menu = alpx_menu)
matmenu.add_command(label = "Density", command = f_mat_dens)
matmenu.add_separator()
matmenu.add_cascade(label = "Operate", menu = operate_menu)
work_plane_menu.add_cascade(label = "Offset WP to...", menu = offset_wp_menu)
work_plane_menu.add_cascade(label = "Align WP with...", menu = align_wp_menu)
work_plane_menu.add_separator()
work_plane_menu.add_cascade(label = "Change Active CS to...", menu = change_active_CS)
work_plane_menu.add_cascade(label = "Change Display CS to...", menu = change_display_CS)
work_plane_menu.add_cascade(label = "Local Coordinate Systems...", menu = local_CS)
local_CS.add_cascade(label = "Create Local CS", menu = create_local_CS)
local_CS.add_command(label = "Delete Local CS...", )

# create widgets
t1_output = ScrolledText(root,
                 width = 123,
                 height = 30,
                 font = ("Verdana", 10, "normal"),
                 bg = 'white',
                 fg = 'black',
                 tabstyle = 'tabular',
                 wrap = WORD
                 )
t1_output.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 2)

t2_solver = ScrolledText(root,
                 width = 123,
                 height = 12,
                 font = ("Verdana", 10, "normal"),
                 bg = 'white',
                 fg = 'black',
                 tabstyle = 'tabular',
                 wrap = WORD
                 )
t2_solver.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 1)


lab1 = Label(root,
             width = 123,
             height = 1,
             bg = 'white',
             fg = 'black',
             font = ("Verdana", 10, "normal"),
             anchor = W
             )
lab1.grid(row = 4, columnspan = 2, sticky = W, padx = 10, pady = 10)

# Start PyMAPDL
jname = 'file'
path = os.getcwd()
mapdl = launch_mapdl(nproc = 4, run_location = path, jobname = jname)
t1_output.delete(1.0, END)
t2_solver.delete(1.0, END)
t2_solver.insert(1.0, mapdl)
t2_solver.yview(END)
lab1['text'] = "PyMAPDL is running..."

mapdl.clear()
enter_prep7 = mapdl.prep7()
t2_solver.insert(END, "\n ")
t2_solver.insert(END, enter_prep7)
t2_solver.yview(END)


# keyboards hotkeys (Main Menu)
# close root window by 'Ctrl+Q'
keyboard.add_hotkey('ctrl+q', f_win_destroy)

# create new ptoject by 'Ctrl+N'
keyboard.add_hotkey('ctrl+n', f_win_newProject)

# open Ansys Classic GUI by 'Ctrl+O'
keyboard.add_hotkey('ctrl+o', f_openAnsysGUI)

# save Ansys database (*.db) by 'Ctrl+S'
keyboard.add_hotkey('ctrl+s', f_save_DB)

# save All Ansys database (*.db) by 'Ctrl+A'
keyboard.add_hotkey('ctrl+a', f_save_ALL)

# clear PyMAPDL
keyboard.add_hotkey('ctrl+c', f_win_startPyMAPDL)

# stop PyMAPDL by 'Ctrl+B'
keyboard.add_hotkey('ctrl+b', f_stopPyMAPDL)

# resume the Ansys database by 'Ctrl+R'
keyboard.add_hotkey('ctrl+r', f_resume)

# Call the mainloop of Tk
root.mainloop()
