all_tickers = ['AA', 'AAPL', 'ABT', 'ABX', 'ADSK', 'TAP', 'ACI', 'ACV', 'ADBE', 'ADI', 'ADM', 'AEM', 'AEP', 'AES', 'AET', 'AFL', 'AGCO', 'AGN', 'HES', 'AIG', 'ALU', 'ALTR', 'AMAT', 'BEAM', 'AMD', 'TWX', 'AMGN', 'AMLN', 'AMR', 'AON', 'APA', 'APC', 'APD', 'APH', 'ARG', 'ASH', 'ATML', 'AU', 'ADP', 'AVP', 'AXP', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBY', 'BCR', 'BCS', 'BDK', 'BDX', 'BEC', 'BEN', 'BHI', 'BHP', 'BJS', 'BK', 'BKE', 'BMC', 'BMY', 'BNI', 'BNS', 'BPL', 'BPOP', 'BRK', 'BSX', 'CA', 'CAG', 'CAT', 'CB', 'CBE', 'CBI', 'CCE', 'C', 'CDE', 'CAH', 'CELG', 'CEPH', 'CERN', 'CI', 'CL', 'CLF', 'CLX', 'CMA', 'CMCS', 'CMCS', 'CMS', 'CNW', 'COG', 'COMS', 'COST', 'CP', 'CPB', 'CRUS', 'CSC', 'CSCO', 'CSX', 'CTL', 'CMI', 'CVC', 'CX', 'CY', 'FTR', 'D', 'DBD', 'DD', 'DE', 'DHR', 'DIA', 'DIS', 'DOV', 'DOW', 'DRE', 'DHI', 'DTE', 'DUK', 'DVN', 'DV', 'ECL', 'ED', 'ELN', 'EMC', 'EMR', 'KMP', 'EOG', 'EP', 'EQT', 'EA', 'ESRX', 'ESV', 'ETN', 'ETR', 'EXPD', 'F', 'FAST', 'M', 'FDO', 'FDX', 'FISV', 'FITB', 'FST', 'S', 'NEE', 'FRX', 'FWLT', 'GCI', 'GD', 'GE', 'GENZ', 'AXLL', 'GILD', 'GIS', 'GLW', 'GSK', 'GPS', 'GR', 'GRA', 'GT', 'GWW', 'HAL', 'MNST', 'HAS', 'HBAN', 'HBHC', 'HCN', 'HCP', 'HD', 'HOG', 'HL', 'HMA', 'HMSY', 'HNZ', 'HFC', 'HOLX', 'HOT', 'HP', 'HRB', 'HRL', 'HSY', 'HUM', 'HPQ', 'IBM', 'BIIB', 'IGT', 'INTC', 'IP', 'IPG', 'IR', 'ITW', 'JBHT', 'JCI', 'JCP', 'JEC', 'JKHY', 'JNJ', 'K', 'KBH', 'KEY', 'KIM', 'KLAC', 'KMB', 'KO', 'KR', 'KSS', 'KSU', 'LEN', 'LLTC', 'LLY', 'LM', 'LNC', 'LOW', 'LPX', 'LRCX', 'LSI', 'LTD', 'L', 'LUFK', 'LUV', 'LZ', 'SM', 'MAS', 'MAT', 'MBI', 'MCD', 'MDC', 'MDT', 'CVS', 'MFC', 'MGA', 'MGM', 'MHFI', 'MIL', 'MMC', 'MMM', 'MO', 'MHK', 'MSI', 'MI', 'MRK', 'MRO', 'MSFT', 'MTG', 'MTB', 'MU', 'MUR', 'MXIM', 'MYL', 'NAV', 'NBL', 'NBR', 'NE', 'NDSN', 'NEM', 'NI', 'NKE', 'THC', 'JWN', 'NOC', 'NSC', 'NSM', 'NTRS', 'NU', 'NUE', 'NVLS', 'NWL', 'FOX', 'OI', 'OKE', 'OMC', 'ORCL', 'OSK', 'OXY', 'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCL', 'PCP', 'PEG', 'PEP', 'PFE', 'PG', 'PGR', 'PH', 'PHM', 'PLL', 'PNC', 'PNM', 'PNR', 'POT', 'PPG', 'PPL', 'PDE', 'PRGO', 'PL', 'PVH', 'PX', 'QCOM', 'RAD', 'RDC', 'REGN', 'RGLD', 'RJF', 'ROK', 'ROP', 'ROST', 'RTN', 'RIO', 'RYL', 'T', 'SBUX', 'SCHW', 'SEE', 'SFD', 'SHW', 'SI', 'SII', 'SLB', 'HSH', 'SLM', 'SNE', 'PII', 'SNV', 'SO', 'TRV', 'SPLS', 'SPW', 'NVE', 'STT', 'SAN', 'STEC', 'STI', 'STJ', 'STR', 'SYK', 'SUN', 'JAVA', 'SVU', 'SWK', 'SWN', 'SWY', 'SY', 'SYMC', 'SYY', 'TE', 'TEF', 'TER', 'TEVA', 'TEX', 'TIF', 'TJX', 'TLAB', 'TMO', 'TOL', 'TOT', 'TM', 'TRA', 'TRMB', 'TROW', 'TSO', 'TXN', 'TXT', 'TYC', 'TSN', 'UBS', 'UDR', 'UN', 'UNH', 'UNM', 'UNP', 'UTX', 'VAR', 'VFC', 'CBS', 'VLO', 'VMC', 'VNO', 'VOD', 'VRTX', 'WAG', 'WDC', 'WFC', 'WFM', 'WHR', 'WMB', 'WMT', 'WSM', 'WY', 'X', 'XL', 'XLNX', 'XOM', 'XRX', 'FL', 'ZION', 'CREE', 'CHK', 'DDR', 'SPY', 'ACT', 'ACE', 'INTU', 'MCHP', 'FOSL', 'GGP', 'JBL', 'ORLY', 'RCL', 'RIG', 'XTO', 'BDN', 'FLIR', 'KGC', 'PETM', 'BWA', 'EQR', 'BKS', 'CAL', 'GMCR', 'ATVI', 'DECK', 'GFI', 'HST', 'PRE', 'NFX', 'PTEN', 'URBN', 'HGSI', 'SPG', 'SU', 'TQNT', 'EMN', 'HAIN', 'MLM', 'TSCO', 'AKS', 'ALB', 'VRX', 'FLEX', 'MAC', 'RKT', 'AEO', 'BRK', 'EXP', 'GDI', 'RAH', 'VVUS', 'GGB', 'NOK', 'CLI', 'ACS', 'SIRI', 'O', 'SSYS', 'COF', 'FOXA', 'VECO', 'MCK', 'SWC', 'STM', 'ASML', 'DLTR', 'FMER', 'LMT', 'AGU', 'DRI', 'LH', 'MDY', 'DDD', 'DISH', 'PAAS', 'CAM', 'FCX', 'SUNE', 'DO', 'PCYC', 'WLT', 'EL', 'LXK', 'NTAP', 'SNDK', 'WAT', 'CTXS', 'HIG', 'ITT', 'SPN', 'SCCO', 'ALXN', 'EIX', 'IRM', 'CCJ', 'CENX', 'EWA', 'EWC', 'EWG', 'EWH', 'EWJ', 'EWW', 'CRR', 'OLED', 'YHOO', 'ONXX', 'CHKP', 'QGEN', 'TIE', 'STRA', 'ETFC', 'LAMR', 'SRCL', 'TD', 'ANF', 'OCN', 'DNR', 'NUS', 'STLD', 'OVIP', 'CNI', 'DGX', 'CIEN', 'KMX', 'AMTD', 'IVZ', 'ROVI', 'ALV', 'AMZN', 'BBT', 'BEXP', 'BXP', 'MS', 'Q', 'CTV', 'FLS', 'MT', 'PXD', 'SLG', 'AYE', 'CHRW', 'NLY', 'PWER', 'TLM', 'TSM', 'YUM', 'AMG', 'FE', 'SID', 'URI', 'VRSN', 'ARMH', 'BRCM', 'FTO', 'LNT', 'FMX', 'LLL', 'VTR', 'WCN', 'AVB', 'CTSH', 'KG', 'EPD', 'PLD', 'RSG', 'RX', 'WM', 'RRC', 'SAP', 'CCI', 'WFT', 'PFCB', 'XLB', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLU', 'XLV', 'XLY', 'BP', 'NVDA', 'DLM', 'EWBC', 'LIFE', 'BBRY', 'INFY', 'PBG', 'PCLN', 'QQQ', 'NUAN', 'AZN', 'INFA', 'BRCD', 'CEG', 'GS', 'PNRA', 'FFIV', 'JNPR', 'RDN', 'RAI', 'SBAC', 'SKX', 'BMRN', 'HSBC', 'HCBK', 'JDSU', 'MDRX', 'TIBX', 'RHT', 'AKAM', 'BLK', 'PKG', 'FNSR', 'PTV', 'QCOR', 'UPS', 'TGT', 'IBN', 'SLAB', 'EW', 'MET', 'ONNN', 'PTR', 'SINA', 'EWY', 'IJH', 'IJR', 'IVV', 'IVW', 'IWB', 'IWD', 'IWF', 'IWM', 'IYF', 'NVS', 'RSH', 'SMH', 'CYH', 'DNDN', 'EWT', 'IYM', 'IYR', 'MBT', 'MRVL', 'NTES', 'VALE', 'RKH', 'ARNA', 'CNQ', 'ENDP', 'EWZ', 'EZU', 'ILMN', 'IWN', 'IWO', 'SOHU', 'VZ', 'PBR', 'SJM', 'XEL', 'ABV', 'LNG', 'COH', 'DVA', 'EXC', 'MCO', 'MON', 'OEF', 'SNP', 'GG', 'NXY', 'NYCB', 'GRMN', 'MEE', 'PGN', 'UPL', 'AMX', 'GPN', 'IBB', 'ICF', 'OIH', 'OIS', 'PBR', 'ABB', 'BTU', 'RTH', 'VTI', 'ADS', 'CVI', 'FTI', 'MDLZ', 'STO', 'FIS', 'COL', 'IWR', 'IWS', 'ABC', 'BG', 'EFA', 'JOY', 'ECA', 'ZMH', 'CIG', 'CS', 'WLP', 'CVX', 'DB', 'EPP', 'IGE', 'ILF', 'PFG', 'AAP', 'WTW', 'CNC', 'PRU', 'GME', 'ITUB', 'ACL', 'VALE', 'ARO', 'NFLX', 'HEW', 'SWKS', 'IEF', 'LQD', 'GOLD', 'SHY', 'SNY', 'TLT', 'COP', 'CNP', 'DKS', 'ERIC', 'PALM', 'PXP', 'WYNN', 'XEC', 'CME', 'EQIX', 'IAG', 'STX', 'TS', 'EGO', 'NIHD', 'CCL', 'EEM', 'A', 'CNX', 'AMT', 'SRE', 'AEE', 'PLD', 'OUTR', 'NOV', 'GES', 'EBAY', 'APOL', 'ESI', 'RL', 'FLR', 'ALL', 'ATI', 'STZ', 'MWW', 'PSA', 'JPM', 'USB', 'CHL', 'HON', 'JEF', 'BBL', 'BTI', 'DELL', 'ISRG', 'AMED', 'MHS', 'AGG', 'ACN', 'IYT', 'DVY', 'TRQ', 'WLL', 'AUY', 'CTRP', 'NG', 'TIP', 'TPX', 'MAR', 'TRW', 'DIG', 'ATHR', 'ETP', 'DTV', 'BBD', 'NRG', 'HOS', 'SHLD', 'HSP', 'GNW', 'CBG', 'CRM', 'MFE', 'NETL', 'HK', 'VMED', 'BUCY', 'GOOG', 'IOC', 'TTM', 'VNQ', 'FXI', 'MOS', 'DLR', 'MTL', 'GLD', 'LVS', 'HLF', 'CE', 'IAU', 'DRYS', 'WIN', 'HUN', 'ANR', 'VGK', 'VWO', 'PAY', 'LBTY', 'THS', 'LEAP', 'SLW', 'FMCN', 'RDS', 'DMND', 'RDS', 'BIDU', 'EXPE', 'CF', 'ROC', 'LBTY', 'LCC', 'AMP', 'FNF', 'KBE', 'SDY', 'ICE', 'SPWR', 'UA', 'ICO', 'VIAB', 'FXE', 'STP', 'LINE', 'WNR', 'CMG', 'UAL', 'DBC', 'HS', 'XHB', 'XCO', 'GPOR', 'ME', 'NYX', 'MDVN', 'HIMX', 'USO', 'VIG', 'SLV', 'TCK', 'ITB', 'LINT', 'GDX', 'MA', 'SH', 'DDM', 'SSO', 'QLD', 'XME', 'XRT', 'KRE', 'XOP', 'KOG', 'CTRX', 'JCG', 'QID', 'SDS', 'DXD', 'WYN', 'HBI', 'WU', 'OC', 'RVBD', 'WCRX', 'PFF', 'EVEP', 'APKT', 'CSIQ', 'HTZ', 'FSLR', 'SE', 'IPGP', 'TSL', 'MPEL', 'DBA', 'TWC', 'CSJ', 'SHV', 'RWM', 'UWM', 'TWM', 'UYM', 'UYG', 'URE', 'DUG', 'SRS', 'SKF', 'JASO', 'MLNX', 'FXY', 'UUP', 'VEU', 'ARUN', 'BSV', 'BND', 'HYG', 'UNG', 'TMUS', 'DAL', 'RSX', 'VRUS', 'CLR', 'LDK', 'YGE', 'COV', 'DFS', 'TEL', 'BX', 'DXJ', 'VEA', 'LULU', 'CXO', 'MELI', 'VMW', 'MOO', 'TDC', 'PCX', 'RF', 'ULTA', 'EEV', 'SD', 'FXP', 'SFSF', 'SOA', 'JNK', 'EMB', 'CPN', 'EPI', 'PM', 'V', 'ACWI', 'DPS', 'TBT', 'CFX', 'AGNC', 'LO', 'DTO', 'RAX', 'WPRT', 'DISC', 'ERY', 'FAZ', 'FAS', 'SPXS', 'TZA', 'ERX', 'SPXL', 'TNA', 'EUO', 'UCO', 'SCO', 'ZSL', 'AGQ', 'EDC', 'TECL', 'EDZ', 'VXX', 'MJN', 'AMJ', 'OPEN', 'SPXU', 'UPRO', 'BUD', 'DRN', 'AVGO', 'TBF', 'CFN', 'SGOL', 'AONE', 'BSBR', 'TWO', 'LEA', 'GDXJ', 'DG', 'FTNT', 'CLD', 'AOL', 'BAC', 'CIT', 'CIE', 'CHTR', 'C', 'SQQQ', 'TQQQ', 'F', 'MERU', 'SSNC', 'SDRL', 'LYB', 'QEP', 'OAS', 'TSLA', 'MCP', 'NXPI', 'AMLP', 'VOO', 'CCSC', 'ELT', 'SODA', 'GM', 'TVIX', 'XIV', 'NUGT', 'DUST', 'DANG', 'YOKU', 'FLT', 'MMI', 'VIXY', 'NLSN', 'KMI', 'BKLN', 'HCA', 'QIHU', 'APO', 'GNC', 'SPLV', 'LNKD', 'MOS', 'YNDX', 'FIO', 'P', 'MPC', 'Z', 'SVXY', 'UVXY', 'GRPN', 'DLPH', 'TRIP', 'KORS', 'ZNGA', 'OIH', 'SMH', 'BOND', 'YELP', 'PSX', 'SPLK', 'FB', 'NOW', 'PANW', 'ADT', 'KRFT', 'RLGY', 'WDAY', 'ABBV', 'SCTY', 'LMCA', 'ZTS', 'PF', 'CST', 'COTY', 'NWSA', 'COLE', 'LXFT', 'HDS', 'TRMR', 'CDW', 'NDLS', 'RNA', 'COVS', 'MONT', 'PINC', 'VMEM', 'RNG', 'PEGI']
ignores = ['ACV', 'BDK', 'BEC', 'BJS', 'BNI', 'BRK', 'CEPH', 'CMCS', 'CMCS', 'GENZ', 'LZ', 'MI', 'NWL', 'PDE', 'SI', 'SII', 'JAVA', 'SY', 'TRA', 'XTO', 'CAL', 'BRK', 'ACS', 'NUS', 'OVIP', 'CTV', 'AYE', 'KG', 'RX', 'PBG', 'PTV', 'SMH', 'RKH', 'RTH', 'HEW', 'MHS', 'ATHR', 'MFE', 'BUCY', 'LBTY', 'RDS', 'RDS', 'LBTY', 'ICO', 'STP', 'ME', 'LINT', 'JCG', 'RSX', 'PCX', 'DISC', 'ELT', 'SMH']

tickers = list(set(all_tickers) - set(ignores))