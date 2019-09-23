#############################################################################
# Generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#  Jun 07, 2019 01:34:37 PM CEST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m118" -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 472x414+970+412
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 5124 1401
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "CheckIt"
    vTcl:DefineAlias "$top" "CheckIt" vTcl:Toplevel:WidgetProc "" 1
    entry $top.ent43 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent43" "Name" vTcl:WidgetProc "CheckIt" 1
    entry $top.ent44 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black -state readonly 
    vTcl:DefineAlias "$top.ent44" "Date" vTcl:WidgetProc "CheckIt" 1
    entry $top.ent45 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black \
        -textvariable Type_1 
    vTcl:DefineAlias "$top.ent45" "Type_1" vTcl:WidgetProc "CheckIt" 1
    entry $top.ent46 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent46" "Type_2" vTcl:WidgetProc "CheckIt" 1
    entry $top.ent47 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$top.ent47" "Type_3" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che48 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text AP -variable CBL_1 
    vTcl:DefineAlias "$top.che48" "CBL_1" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che49 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text BL -variable che48 
    vTcl:DefineAlias "$top.che49" "CBL_2" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che50 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text DD -variable che48 
    vTcl:DefineAlias "$top.che50" "CBL_3" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che51 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text ID -variable che48 
    vTcl:DefineAlias "$top.che51" "CBL_4" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che52 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text KD -variable che48 
    vTcl:DefineAlias "$top.che52" "CBL_5" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che53 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text KZ -variable che48 
    vTcl:DefineAlias "$top.che53" "CBL_6" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che54 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text ME -variable che48 
    vTcl:DefineAlias "$top.che54" "CBL_7" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che55 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text MP -variable che48 
    vTcl:DefineAlias "$top.che55" "CBL_8" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che56 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text PH -variable che48 
    vTcl:DefineAlias "$top.che56" "CBL_9" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che57 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text PL -variable che48 
    vTcl:DefineAlias "$top.che57" "CBL_10" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che58 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text RS -variable che48 
    vTcl:DefineAlias "$top.che58" "CBL_11" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che59 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text WH -variable che48 
    vTcl:DefineAlias "$top.che59" "CBL_12" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che60 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text WN -variable che48 
    vTcl:DefineAlias "$top.che60" "CBL_13" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che61 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text WD -variable che48 
    vTcl:DefineAlias "$top.che61" "CBL_14" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che62 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text WZ -variable che48 
    vTcl:DefineAlias "$top.che62" "CBL_15" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che63 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -textvariable Type_1 -variable CBT1_1 
    vTcl:DefineAlias "$top.che63" "CBT1_1" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che64 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable Type_1 
    vTcl:DefineAlias "$top.che64" "CBT1_2" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che65 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che65" "CBT1_3" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che66 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che66" "CBT1_4" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che67 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che67" "CBT1_5" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che68 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che68" "CBT1_6" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che69 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che69" "CBT1_7" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che70 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che70" "CBT1_8" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che71 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che71" "CBT1_9" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che72 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che72" "CBT1_10" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che73 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che73" "CBT1_11" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che74 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che74" "CBT1_12" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che75 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che75" "CBT1_13" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che76 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che76" "CBT1_14" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che77 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che77" "CBT1_15" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che78 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -textvariable Type_1 -variable CBT2_1 
    vTcl:DefineAlias "$top.che78" "CBT2_1" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che79 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che79" "CBT2_2" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che80 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che80" "CBT2_3" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che81 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che81" "CBT2_4" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che82 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che82" "CBT2_5" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che83 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che83" "CBT2_6" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che84 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che84" "CBT2_7" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che85 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che85" "CBT2_8" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che86 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che86" "CBT2_9" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che87 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che87" "CBT2_10" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che88 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che88" "CBT2_11" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che89 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che89" "CBT2_12" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che90 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che90" "CBT2_13" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che91 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che91" "CBT2_14" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che92 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che92" "CBT2_15" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che93 \
        -activebackground {#ececec} -activeforeground {#000000} -anchor w \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -textvariable Type_1 -variable CBT3_1 
    vTcl:DefineAlias "$top.che93" "CBT3_1" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che94 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che94" "CBT3_2" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che95 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che95" "CBT3_3" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che96 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che96" "CBT3_4" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che97 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che97" "CBT3_5" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che98 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che98" "CBT3_6" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che99 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che99" "CBT3_7" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che100 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che100" "CBT3_8" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che101 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che101" "CBT3_9" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che102 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che102" "CBT3_10" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che103 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che103" "CBT3_11" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che104 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che104" "CBT3_12" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che105 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che65 
    vTcl:DefineAlias "$top.che105" "CBT3_13" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che111 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che111 
    vTcl:DefineAlias "$top.che111" "CBT3_14" vTcl:WidgetProc "CheckIt" 1
    checkbutton $top.che112 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Check -variable che112 
    vTcl:DefineAlias "$top.che112" "CBT3_15" vTcl:WidgetProc "CheckIt" 1
    button $top.but116 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Save 
    vTcl:DefineAlias "$top.but116" "Save" vTcl:WidgetProc "CheckIt" 1
    button $top.but117 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Open 
    vTcl:DefineAlias "$top.but117" "Open" vTcl:WidgetProc "CheckIt" 1
    set site_3_0 $top.m118
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    $site_3_0 add command \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command {} -font TkMenuFont \
        -foreground {#000000} -label Open 
    $site_3_0 add command \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -command {} -font TkMenuFont \
        -foreground {#000000} -label Save 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent43 \
        -in $top -x 20 -y 10 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 140 -y 10 -width 114 -height 20 -anchor nw \
        -bordermode ignore 
    place $top.ent45 \
        -in $top -x 80 -y 70 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 200 -y 70 -width 114 -height 20 -anchor nw \
        -bordermode ignore 
    place $top.ent47 \
        -in $top -x 320 -y 70 -width 114 -height 20 -anchor nw \
        -bordermode ignore 
    place $top.che48 \
        -in $top -x 10 -y 100 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che49 \
        -in $top -x 10 -y 120 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che50 \
        -in $top -x 10 -y 140 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che51 \
        -in $top -x 10 -y 160 -width 61 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che52 \
        -in $top -x 10 -y 180 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che53 \
        -in $top -x 10 -y 200 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che54 \
        -in $top -x 10 -y 220 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che55 \
        -in $top -x 10 -y 240 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che56 \
        -in $top -x 10 -y 260 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che57 \
        -in $top -x 10 -y 280 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che58 \
        -in $top -x 10 -y 300 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che59 \
        -in $top -x 10 -y 320 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che60 \
        -in $top -x 10 -y 340 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che61 \
        -in $top -x 10 -y 360 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che62 \
        -in $top -x 10 -y 380 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che63 \
        -in $top -x 80 -y 100 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che64 \
        -in $top -x 80 -y 120 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che65 \
        -in $top -x 80 -y 140 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che66 \
        -in $top -x 80 -y 160 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che67 \
        -in $top -x 80 -y 180 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che68 \
        -in $top -x 80 -y 200 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che69 \
        -in $top -x 80 -y 220 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che70 \
        -in $top -x 80 -y 240 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che71 \
        -in $top -x 80 -y 260 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che72 \
        -in $top -x 80 -y 280 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che73 \
        -in $top -x 80 -y 300 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che74 \
        -in $top -x 80 -y 320 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che75 \
        -in $top -x 80 -y 340 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che76 \
        -in $top -x 80 -y 360 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che77 \
        -in $top -x 80 -y 380 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che78 \
        -in $top -x 200 -y 100 -width 111 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che79 \
        -in $top -x 200 -y 120 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che80 \
        -in $top -x 200 -y 140 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che81 \
        -in $top -x 200 -y 160 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che82 \
        -in $top -x 200 -y 180 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che83 \
        -in $top -x 200 -y 200 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che84 \
        -in $top -x 200 -y 220 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che85 \
        -in $top -x 200 -y 240 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che86 \
        -in $top -x 200 -y 260 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che87 \
        -in $top -x 200 -y 280 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che88 \
        -in $top -x 200 -y 300 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che89 \
        -in $top -x 200 -y 320 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che90 \
        -in $top -x 200 -y 340 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che91 \
        -in $top -x 200 -y 360 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che92 \
        -in $top -x 200 -y 380 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che93 \
        -in $top -x 320 -y 100 -width 121 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che94 \
        -in $top -x 320 -y 120 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che95 \
        -in $top -x 320 -y 140 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che96 \
        -in $top -x 320 -y 160 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che97 \
        -in $top -x 320 -y 180 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che98 \
        -in $top -x 320 -y 200 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che99 \
        -in $top -x 320 -y 220 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che100 \
        -in $top -x 320 -y 240 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che101 \
        -in $top -x 320 -y 260 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che102 \
        -in $top -x 320 -y 280 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che103 \
        -in $top -x 320 -y 300 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che104 \
        -in $top -x 320 -y 320 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che105 \
        -in $top -x 320 -y 340 -width 61 -height 25 -anchor nw \
        -bordermode ignore 
    place $top.che111 \
        -in $top -x 320 -y 360 -anchor nw -bordermode ignore 
    place $top.che112 \
        -in $top -x 320 -y 380 -anchor nw -bordermode ignore 
    place $top.but116 \
        -in $top -x 350 -y 10 -anchor nw -bordermode ignore 
    place $top.but117 \
        -in $top -x 390 -y 10 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
