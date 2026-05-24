let( ( libName libPath tools)
  
  libName = "smic18mmrf"
  printf("Loading libInitCustomExit.il for %s\n" libName)
  
  libPath = ddGetObjReadPath(ddGetObj(libName))
  
; setup spectre model files, sections
  when( isContextLoaded("schView")
     envSetVal("asimenv.startup" "simulator" 'string "spectre")
     tools = envGetAvailableTools()
     case( libName
	( "smic18mmrf"
	  when( member("spectre" tools)
	     asiSetEnvOptionVal(
		asiGetTool('spectre) "modelFiles"
		list(
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "bjt_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "dio_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "res_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "mim_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "var_tt")
		)
	     )
	  ) ; ** when asiTool **
	  when( member("UltraSim" tools)
	     asiSetEnvOptionVal(
		asiGetTool('UltraSim) "modelFiles"
		list(
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "bjt_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "dio_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "res_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "mim_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "var_tt")
		)
	     )
	  ) ; ** when asiTool **
	  when( member("ams" tools)
	     asiSetEnvOptionVal(
		asiGetTool('ams) "modelFiles"
		list(
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "bjt_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "dio_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "res_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "mim_tt")
		   list(strcat( libPath "/../models/spectre/ms018_enhanced_v1p11_spe.lib") "var_tt")
		)
	     )
	  ) ; ** when asiTool **
	  when( member("hspiceD" tools)
	     asiSetEnvOptionVal(
		asiGetTool('hspiceD) "modelFiles"
		list(
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "TT")
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "BJT_TT")
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "DIO_TT")
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "RES_TT")
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "MIM_TT")
		   list(strcat( libPath "/../models/hspice/ms018_enhanced_v1p11.lib") "VAR_TT")
		)
	     )
	  ) ; ** when asiTool **
	)
     ) ; ** case libName **
  ) ; ** when isContextLoaded **
) ; ** let **
