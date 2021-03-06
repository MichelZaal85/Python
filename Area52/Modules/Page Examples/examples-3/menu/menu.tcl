#############################################################################
# Generated by PAGE version 4.8.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


vTcl:font:add_GUI_font font10 \
"-family {DejaVu Sans} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) wheat
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top32
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.m33
    set site_3_0 $base.m33
    set site_4_0 $site_3_0.men32
    set site_5_0 $site_4_0.men32
    set site_6_0 $site_5_0.men32
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
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top32 {base} {
    if {$base == ""} {
        set base .top32
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m33" -background wheat -highlightbackground wheat \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 644x420+648+140
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel 1"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure Menu -background wheat
    ttk::style configure Menu -foreground #000000
    ttk::style configure Menu -font font9
    menu $top.m33 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $top.m33 add cascade \
        -menu "$top.m33.men34" -background {#00ffff} -compound left \
        -font {-family Purisa -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground {#000000} -label File 
    set site_3_0 $top.m33
    menu $site_3_0.men34 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $site_3_0.men34 add command \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#ffff00} -command {#save} -compound none \
        -font TkMenuFont -foreground {#000000} -image {} -label Save 
    $site_3_0.men34 add separator \
        -background {#ffff00} 
    $site_3_0.men34 add command \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#ffff00} -command {#quit} -compound top -font TkMenuFont \
        -foreground {#000000} \
        -image [vTcl:image:get_image [file join stop.gif]] -label Quit 
    $top.m33 add cascade \
        -menu "$top.m33.men32" -background {#990000} \
        -font {-family Purisa -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground {#ffff00} -label Edit 
    set site_3_0 $top.m33
    menu $site_3_0.men32 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $site_3_0.men32 add command \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#ff0000} -command {#cut} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -foreground white -label Cut 
    $site_3_0.men32 add command \
        -activebackground {#d9d9d9} -activeforeground black \
        -background {#ff0000} -command {#copy} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -foreground white -label Copy 
    $site_3_0.men32 add separator \
        -background {#ff0000} 
    $site_3_0.men32 add command \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#ff0000} -command {#paste} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -foreground white -label Paste 
    $site_3_0.men32 add cascade \
        -menu "$site_3_0.men32.men32" -activebackground white \
        -activeforeground {#000000} -background {#ff0000} -command {} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -foreground white -label Other 
    set site_4_0 $site_3_0.men32
    menu $site_4_0.men32 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $site_4_0.men32 add command \
        -background {#ffff00} -command {#post} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label Post 
    $site_4_0.men32 add command \
        -background {#ffff00} -command {#sync} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label Sync 
    $site_4_0.men32 add cascade \
        -menu "$site_4_0.men32.men32" -background {#ffff00} -command {} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label Still 
    set site_5_0 $site_4_0.men32
    menu $site_5_0.men32 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $site_5_0.men32 add command \
        -background plum -command {#yes} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label Yes 
    $site_5_0.men32 add command \
        -background plum -command {#no} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label No 
    $site_5_0.men32 add checkbutton \
        -variable IRS -background plum -command {} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label IRS 
    $site_5_0.men32 add checkbutton \
        -variable Charity -background plum -command {} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label Charity 
    $site_5_0.men32 add cascade \
        -menu "$site_5_0.men32.men32" -background plum -command {} \
        -font [vTcl:font:getFontFromDescr "-family {DejaVu Sans Mono} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"] \
        -label More 
    set site_6_0 $site_5_0.men32
    menu $site_6_0.men32 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#ff0000} -font TkMenuFont -foreground black -tearoff 0 
    $site_6_0.men32 add radiobutton \
        -selectcolor {} -value Radio_A -variable selectedButton \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#ffff00} -command {#radio_a} -compound none \
        -font TkMenuFont -foreground {#000000} -image {} -label Radio-A 
    $site_6_0.men32 add radiobutton \
        -selectcolor {} -value Radio_B -variable selectedButton \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#00ff00} -command {#radio_b} -compound none \
        -font TkMenuFont -foreground {#000000} -image {} -label Radio-B 
    $site_6_0.men32 add checkbutton \
        -selectcolor {#990000} -variable Check_1 -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#ff0000} -command {#check1} \
        -compound left -font TkMenuFont -foreground {#000000} \
        -image [vTcl:image:get_image [file join openfold.gif]] \
        -label {Check 1} 
    $site_6_0.men32 add checkbutton \
        -selectcolor {} -variable Check_2 -activebackground {#d9d9d9} \
        -activeforeground {#000000} -background {#ff0000} -command {#check2} \
        -compound none -font TkMenuFont -foreground {#000000} -image {} \
        -label {Check 2} 
    ###################
    # SETTING GEOMETRY
    ###################

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top32

