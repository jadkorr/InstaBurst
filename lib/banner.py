# Date: 03/13/2018
# -*- coding: utf-8 -*-
# Author: Ethical-H4CK3R
# Description: Banner Generator

from random import choice 
from constants import _colors as colors, banners_tabs_amt as tabs

banners = []

art1 = r'''                                                                                                                                 
{0}{1} ___                 __        {2}__________ {1}                      __   
{0}{1}|   | ____   _______/  |______ {2}\______   \{1}__ _________  _______/  |_ 
{0}{1}|   |/    \ /  ___/\   __\__  \ {2}|    |  _/{1}  |  \_  __ \/  ___/\   __\
{0}{1}|   |   |  \\___ \  |  |  / __ \{2}|    |   \{1}  |  /|  | \/\___ \  |  |  
{0}{1}|___|___|  /____  > |__| (____  /{2}______  /{1}____/ |__|  /____  > |__|  
{0}{1}         \/     \/            \/{2}       \/ {1}                 \/        
'''

art2 = r'''                                                                                                
{0}{1} ___  ________   ________  _________  ________ {2} ________ {1} ___  ___  ________  ________  _________   
{0}{1}|\  \|\   ___  \|\   ____\|\___   ___\\   __  \{2}|\   __  \{1}|\  \|\  \|\   __  \|\   ____\|\___   ___\ 
{0}{1}\ \  \ \  \\ \  \ \  \___|\|___ \  \_\ \  \|\  \{2} \  \|\ /\{1} \  \\\  \ \  \|\  \ \  \___|\|___ \  \_| 
{0}{1} \ \  \ \  \\ \  \ \_____  \   \ \  \ \ \   __  \{2} \   __  \{1} \  \\\  \ \   _  _\ \_____  \   \ \  \  
{0}{1}  \ \  \ \  \\ \  \|____|\  \   \ \  \ \ \  \ \  \{2} \  \|\  \{1} \  \\\  \ \  \\  \\|____|\  \   \ \  \ 
{0}{1}   \ \__\ \__\\ \__\____\_\  \   \ \__\ \ \__\ \__\{2} \_______\{1} \_______\ \__\\ _\ ____\_\  \   \ \__\
{0}{1}    \|__|\|__| \|__|\_________\   \|__|  \|__|\|__|{2}\|_______|{1}\|_______|\|__|\|__|\_________\   \|__|
{0}{1}                   \|_________|                               {1}                  \|_________|        
                                                                                                    
'''

art3 = ''' 
{0}{1} ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄     {2}  ▄▄▄▄   {1} █    ██  ██▀███    ██████ ▄▄▄█████▓   
{0}{1}▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄   {2} ▓█████▄ {1}██  ▓██▒▓██ ▒ ██▒▒██    ▒ ▓  ██▒ ▓▒   
{0}{1}▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄ {2} ▒██▒ ▄██{1}▓██  ▒██░▓██ ░▄█ ▒░ ▓██▄   ▒ ▓██░ ▒░   
{0}{1}░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██{2} ▒██░█▀  {1}▓▓█  ░██░▒██▀▀█▄    ▒   ██▒░ ▓██▓ ░    
{0}{1}░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██{2}▒░▓█  ▀█▓{1}▒▒█████▓ ░██▓ ▒██▒▒██████▒▒  ▒██▒ ░    
{0}{1}░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█{2}░░▒▓███▀▒{1}░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░  ▒ ░░      
{0}{1} ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ {2}░▒░▒   ░ {1}░░▒░ ░ ░   ░▒ ░ ▒░░ ░▒  ░ ░    ░       
{0}{1} ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒  {2}  ░    ░ {1} ░░░ ░ ░   ░░   ░ ░  ░  ░    ░         
{0}{1} ░           ░       ░                 ░  {2}░ ░      {1}   ░        ░           ░              
{0}{1}                                          {2}       ░                                       
'''

art4 = '''                                                                                                                    
{0}{1}        #####  #                                    {2}      ##### ##                                                  
{0}{1}     ######  /                                      {2}   ######  /##                                                  
{0}{1}    /#   /  /                          #            {2}  /#   /  / ##  {1}                                       #        
{0}{1}   /    /  /                          ##            {2} /    /  /  ##  {1}                                      ##        
{0}{1}       /  /                           ##            {2}     /  /   /   {1}                                      ##        
{0}{1}      ## ## ###  /###      /###     ######## /###   {2}    ## ##  /    {1} ##   ####    ###  /###     /###     ########    
{0}{1}      ## ##  ###/ #### /  / #### / ######## / ###  /{2}    ## ## /     {1} ##    ###  / ###/ #### / / #### / ########     
{0}{1}    /### ##   ##   ###/  ##  ###/     ##   /   ###/ {2}    ## ##/      {1} ##     ###/   ##   ###/ ##  ###/     ##        
{0}{1}   / ### ##   ##    ##  ####          ##  ##    ##  {2}    ## ## ###   {1} ##      ##    ##       ####          ##        
{0}{1}      ## ##   ##    ##    ###         ##  ##    ##  {2}    ## ##   ### {1} ##      ##    ##         ###         ##        
{0}{1} ##   ## ##   ##    ##      ###       ##  ##    ##  {2}    #  ##     ##{1} ##      ##    ##           ###       ##        
{0}{1}###   #  /    ##    ##        ###     ##  ##    ##  {2}       /      ##{1} ##      ##    ##             ###     ##        
{0}{1} ###    /     ##    ##   /###  ##     ##  ##    /#  {2}   /##/     ### {1} ##      /#    ##        /###  ##     ##        
{0}{1}  #####/      ###   ### / #### /      ##   ####/ ## {2}  /  ########   {1}  ######/ ##   ###      / #### /      ##        
{0}{1}    ###        ###   ###   ###/        ##   ###   ##{2} /     ####     {1}   #####   ##   ###        ###/        ##       
{0}{1}                                                    ##                                                              
{0}{1}                                                      ##                                                            
'''

def create(art):
 for _color1 in colors:
  for _color2 in colors:
    for color1 in colors[_color1]:
     for color2 in colors[_color2]:
      banners.append(art.format('\t'*tabs, color2, color1)+ '\033[0m')

def banner():
 return choice(banners) 

create(art1)
create(art2)
create(art3)
create(art4)
 