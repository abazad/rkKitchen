#!/usr/bin/python
#
#   
#   FreakTabKitchen www.freaktab.com
#
#   Copyright 2013 Brian Mahoney brian@mahoneybrian.wanadoo.co.uk
#
############################################################################
#
#   FreakTabKitchen is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FreakTabKitchen is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with FreakTabKitchen.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

import os
import logging


import rominfo
from utils import QueryPickleLoad, PickleIt

#    try:
#        
#    except Exception as e:
#        logging.error('KitchenConfig::mountsystem ' )
#        logging.error(e)
#        raise

class KitchenConfig:
    '''encapsulate info re the ROM''' 
    KitchenPath = ''
    KitchenConfigFile = ''
    initialised = 0
    cwd =''
    
    editor = 'gedit'
    browser = 'nautilus'
    pwidth = 70
    maxsystemsize = 0
    minsystemsize = 0
    defaultsystemsize = 576716800
    
    def __init__(self):
        '''initialise Kithchen Config

        '''
 
        logging.debug('Initialising KitchenConfig')
        try:
            KitchenConfig.KitchenPath = os.path.dirname( os.path.abspath(__file__))
            KitchenConfig.KitchenConfigFile = os.path.join(KitchenConfig.KitchenPath,'Kitchen.config')
            logging.info('KitchenConfig.KitchenPath ' + KitchenConfig.KitchenPath)
            
            #test here to prevent reentry 
            if KitchenConfig.initialised == 0:
                #prevent re-entry
                KitchenConfig.initialised = 1
                
                logging.debug('attemp to pickleload')
                
                #attempt to load a saved config
                reader = KitchenConfig() 
                reader = QueryPickleLoad(reader, reader.KitchenConfigFile)
                
                logging.debug('attemp to pickleload completed')

                #copy values back from the reader
                KitchenConfig.editor = reader.editor
                KitchenConfig.browser = reader.browser
                KitchenConfig.pwidth = reader.pwidth
                KitchenConfig.maxsystemsize = reader.maxsystemsize
                KitchenConfig.minsystemsize = reader.minsystemsize
                KitchenConfig.defaultsystemsize = reader.defaultsystemsize
                
            #copy values into self for pickle useage
            self.editor = KitchenConfig.editor
            self.browser = KitchenConfig.browser 
            self.pwidth = KitchenConfig.pwidth 
            self.maxsystemsize = KitchenConfig.maxsystemsize 
            self.minsystemsize = KitchenConfig.minsystemsize 
            self.defaultsystemsize = KitchenConfig.defaultsystemsize 
            
        except Exception as e:
            logging.error('KitchenConfig::__init__ ' )
            logging.error(e)
            raise
 
 #Static methods   
    @staticmethod
    def KitchenFolders():
        '''static list of required folders for kitchen
        '''
        
        folders = [  'localdeploy'
                    ,'working/mntsystem'
                    ,'working/mntsystem_ext4'
                    ,'working/boot'
                    ,'working/brand'
                    ,'working/removed'
                    ,'KitchenPrivate'
                    ,'read'
                    ]
        return folders
 
    
    @staticmethod    
    def ROMInfoLoc():
        '''static location of rominfo file
        '''
        return 'KitchenPrivate/ROMInfo.rtb'
 
        
    @staticmethod
    def SourceROMLoc():
        '''static location of source ROM
        '''
        return os.path.join('sources',rominfo.rominfo.romname)
 
        
    @staticmethod
    def SourceROMUnpackedLoc():
        '''static location of unpacked source ROM
        '''
        return os.path.join(KitchenConfig.SourceROMLoc(),'unpacked')

    
    @staticmethod    
    def Pickle():
        '''static pickle the KitchenConfig
        '''
        reader = KitchenConfig() 
        PickleIt(reader, KitchenConfig.KitchenConfigFile)
    
