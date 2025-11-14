6500 and CPL Site Manager

Note: Please refer to Planning and Installation guide for HP and Sun workstations minimum and recommended hardware requirements and Site Manager Installation instructions.

Software Installation Requirements and Instructions 

Recommended PC Hardware Requirements: 
	
	        Windows XP operating system:
		400 MB of free hard disk space
		Pentium processor at 400 MHz or higher
		256 or higher MB RAM memory
		CD-ROM drive or network connection
		256-color display

	Windows Vista operating system:
		1GHZ 32-bit(x86) processor
		1GB RAM
		40GB hard drive space       
		Graphics adapter (Direct 9 support, WDDM Driver, 128MB video RAM, Pixel Shader 2.0 hardware support, 32-bits 			per pixel)
		DVD-ROM drive 


Site Manager font display issue on certain PC configurations

Issue:  on some PC configurations with non standard font configurations the text within Site Manager may be difficult to read.  Specifically the fonts will appear shifted as a result of excess padding below the text.
If you are encountering this problem use this procedure to change the Site Manager font mappings.

1 Install Site Manager (if not already installed).
2 Close all Site Manager sessions on the PC.
3 Using Windows Explorer locate the directory in which Site Manager is installed.  Referred to as <install dir> below.
	- The default directory is C:\Program Files\Site Manager\
4 Locate the following file in the installation directory: <install dir>/sm_other_font.properties
5 Copy this file to the following location: <install dir>/jre<X.Y.Z_ab>/lib/      
where <X.Y.Z_ab> represents the version of the installed JRE
	note: admin rights might be required to copy files in the C:/Program Files directory
6 Rename the file in Step 5 to: 'fontconfig.<OS>.properties'
where OS = XP if the PC is running Windows XP
where OS = vista if the PC is running Windows Vista

  end 
