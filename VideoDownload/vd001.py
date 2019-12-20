import requests

chunk_size = 256

url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_00_01_WX30_Welcome.mp4?c3.ri=3775388175057077100&hashval=1576876075_0b6e6d109cb1df9a65e54d67b10dd1a0'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_02_XR30_GeneralTips.mp4?c3.ri=3775669647085197673&hashval=1576876715_40d8d3ddc127600f9d0b12e8f241ec86'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_03_XR30_MeasuringTime.mp4?c3.ri=3773980798374171856&hashval=1576877034_307ef021e8231265748b02b89883370b'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_04_XR30_CPUProfiling.mp4?c3.ri=3773417848018099185&hashval=1576877249_50c5b47b458955fc92d2dce82701dd4c'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_05_XR30_lineprofiler.mp4?c3.ri=3775106698620753748&hashval=1576877326_bd6562258b1bea4b60e2ce3d8a2a594e'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_06_XR30_tracingmemory.mp4?HlSiky_V6F6avgZOOfFC1SsIirpYwla3b01Qqp36OgQGULq03Rm2ujZfiey64uhwQzhRPuBHAwFjc7KkFqPCcgX1xQUnaVk_W7IbchDouG9Ljrz19tg7GGfowRVMcDAbTaiDI7X5MC627_oMbbSSIUQIyoO2VidBOc3o0WsBtq3jzhu7e62nUVugFjwsmHdvSlc&c3.ri=3776514363640283406'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_02_01_XR30_BigONotation.mp4?c3.ri=3776514363640283758&hashval=1576877495_90a8c8fd741a40663221d6acc037bca9'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_02_02_XR30_bisect.mp4?c3.ri=3773699322697014986&hashval=1576877592_83d08ff5fb36bb64fcb473b9b576ab77'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_02_03_XR30_deque.mp4?c3.ri=3773417848018100213&hashval=1576877651_080f10098ef6bf1a8697e1f2b443ee16'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_02_04_XR30_heapq.mp4?c3.ri=3773699322697015345&hashval=1576877736_30b5bb64d5ba2531d3a7fee12a25bfaa'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_02_05_XR30_BeyondStandard.mp4?c3.ri=3775388175057081551&hashval=1576877800_52b34ac2039d310632274aa2e1ec0194'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_03_01_XR30_LocalCaching.mp4?c3.ri=3776232598389185973&hashval=1576877876_809483e9c6ab2f56325d9097242a75da'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_03_02_XR30_RemoveFunctionCalls.mp4?c3.ri=3775669647085200831&hashval=1576877936_d7facf16a36eaa061a7e83be3164f7ca'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_03_03_XR30_usingslotsb.mp4?c3.ri=3773980798374174409&hashval=1576878008_e094b1b41a1c48c8955849b6ea669574'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_03_04_XR30_builtins.mp4?c3.ri=3774262273178919203&hashval=1576878065_b90ad30101941156643ee870d7c1ffbe'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_03_05_XR30_Allocate.mp4?Ng_WUVJwAj3KceI5Uni-j_t60WGOlb2_SdG5QEjBm0WxuNgQF_W42Mjov1S4NHtN4oFyvsnmNW1BTQ8jRyRN3wA7ziTKhr81KaAsX2sPZMPlT5Ln4gliITxk-IIOpNUEm6Q2pUI8VfX0OpZACFJyNOQ4xVLs_5ge9HZwJE9bY7vJCa4rk3D6vCd1AiM&c3.ri=3774543749669771186'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_04_01_XR30_Overview.mp4?NtI854iPo7QdG9kxhs1TncVj1pd0l3FWUho09cOwoII8sToolE5SoQgaRCuaqQKTOz4YSpL9uK14frZi64jdTTQ8-4kFtMHlXecEeCxy3d2V5780E1dnS10m-2rnMMSQG-SRqTyjogWFAGx-Jm5MMboULXOjR9Ae8Bu2LfmWNGhF_ENBFMlkWIwkPB7w&c3.ri=3773699322697016775'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_01_XR30_ProfileFirst.mp4?c3.ri=3773980798374175283&hashval=1576878328_3a5e507a42f7d9c260fe1d7f2332a7b1'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_02_XR30_GeneralTips.mp4?c3.ri=3774543749669771970&hashval=1576878406_f77cbd7a6c3e4973ca45db28e68a33a4'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_01_07_XR15_MemoryProfiler.mp4?c3.ri=3773417848018102980&hashval=1576878660_5d59341883462ffa12e4aa063b5922d4'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_04_02_XR30_Precalculating.mp4?c3.ri=3773699322697019030&hashval=1576879077_731ac65465e22b9f410eded164cf2f47'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_04_03_XR30_lru_cache.mp4?c3.ri=3775951121713788663&hashval=1576879130_ddd1a62a74ec547cc71692e5dd809ba3'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_04_04_XR30_joblib.mp4?c3.ri=3773417848018104435&hashval=1576879189_94d10f8bc666115dd7811fb6090047d1'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_05_01_XR30_Approximation.mp4?xcvP-CxGB2EMGwfWoY4NNQrcALhg2cjJqNw5scMKHjAorwJDdE3GlsbahnRh27m0gDbn3V2Rnr_m7mgLbKCuuY44qtPjaH48Z9aBsWXra0AgLqUMzHLKETAepz6A7RTYLy1DuKS5460Qw0hPJ28rQvd_hIH9rIgyGgwO5KRVWhSEBkZ46gN-aoDJI4Kcqad4Yh0&c3.ri=3775669647085204476'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_05_02_XR30_CheatingExample.mp4?8en-QLFNVWcA5F2A2tC2J1icktzv734iRhCa59Cfq-RT2jMWJk5XQrYbPwvfvUkqKDjdzA9t9Ac7bJbx0qUMG0S1uY-gMjqpFIuKzkagVb_TV5_TPP0LkZ6Apoy0VRplyagAenIyTKvrGo2rj763IISQj8QCIOdNXav7cnp61jq7Hik8cDlyDPCc490jkP_UJ2PBWw&c3.ri=3776232598389189911'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_06_01_XR30_AmdahlsLaw.mp4?PSYxp2sDEZay2TiHCsZdV_9_s-ZIkJgk18Ep9millP65YJf83R8oCMB11aAIE04RMOXaK9JttKg8aueJrgMf1suU_9T4xWZOnsZO8VViteq3vv7HuT8V9HnwDXk5PvDMcMJrgtCt0NjmdZKypjbmf0o0CaevUyqtnihkT5NtKuoFzbQsbR1piF3O1Uscxg&c3.ri=3775951121713789391'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_06_02_XR30_Threads.mp4?UwaG4kbohkh1F_iLRcCVX7ns-Hp7wU6oI6ttARQVb5hUkMJWur38IKt1NBu_U4C2sMdzNwBnP1Kgfx2UPS7PwCwEltR14m2bYci1lKEI2J1yQgb1YFcY6Hvc3oqR_rzlzOUMZZiJEYJaOgrh39lUNXrH0Q6qHYYqyj5sCEbm9mvsrXEWP3wGrXSdmYg&c3.ri=3775388175057086119'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_06_03_XR30_Processes.mp4?Rd-gPIGkgTzQZxNqe1T4TMOM0ql5EnI-JBPXi3YAIZWA-2kDFxi4wZ5q5W502v2jTMXZe5R8NV_A5wTwFdpsqrCOPPmA_Jjs_uxjgzkXOog629xEheC6phwwSNzB5NPsp56mmaPJNjd5sM4qCAqhMAN1kYYsjPDhMfr_yZgc5I-UmfvsFXiyfLefHzwL5A&c3.ri=3773417848018105284'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_06_04_XR15_AsyncIO.mp4?d_SUxU_ZhTLNQsoUtUs1fqglchAjPH6GUjKaYmHtrObwWaK0tBj6kpgyYKSTMPHrGQwr8dtbRDAXPyLJMsCTWgdRi9CcrDpBX89fEoAfvqq3ppDWXAm670vM_rAvRRuTH16iUjKC_d9jTK6lRwnUnlytc1MKySis5Z2tH6NyZSu9V-vF5amcgYRa5B8&c3.ri=3775951121713789900'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_07_01_XR30_numpy.mp4?nXgvuKQAick_UsA5s_-8D0V-g4xxeCNsntwC-y9AtDXefKhTP_GaGAqve0wKWNTfzL21XDBtqsdj9vfxfAy4uIkGMHDcE0OdTIBhJ2BKRffnbvPDvNykw0FbC2h4_w8PTkyAid_dRbHI2WHhD3CtZlRz8-MqFPfvhMiWKdqBkmATV9jPG71Y5pH8&c3.ri=3774262273178923521'
url = 'https://files3.lynda.com/secure/courses/661762/VBR_MP4h264_main_SD/661762_07_02_XR30_numba.mp4?ZhOjx4EHiNXQ4NiQpKJh30XsUjc3eFSzg6h2DVZ7ImReEvUKolrqyhrQvnola2PUEs4RIvt0qPrCbhgycoC_1L8Zlalqvw6qHr1VHw1LrSY_cRGwsuBjL-Q2s0hdGkKM2CFeKhyxCJKokKLQrWvwLMJtBPcRVMRI8zNLwOGxXQ35fWz_Z7sqJCdP&c3.ri=3773699322697020730'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_07_03_XR30_Cython.mp4?c3.ri=3773699322697020914&hashval=1576879732_9787618dcd98a449edef4a6257540c49'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_07_04_XR30_pypy.mp4?c3.ri=3773980798374179375&hashval=1576879785_1591097ccea5ebec94d5efca53d13a66'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_07_05_XR30_CExtensions.mp4?c3.ri=3775388175057087276&hashval=1576879832_829bab2cd738bcd0592ef13de3911759'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_08_01_XR30_Process.mp4?c3.ri=3776514363640292983&hashval=1576879944_bb885c7ead87fb6a5fda1e830bd47f0c'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_08_02_XR30_DesignCodeReviews.mp4?c3.ri=3775388175057087696&hashval=1576879989_518331442a816be2eb9653b4ee8b83f6'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_08_03_XR30_Benchmarks.mp4?c3.ri=3775669647085206755&hashval=1576880043_08a44a5eeadff9287f9f3ce94704cfd5'
url = 'https://lynda_files2-a.akamaihd.net/secure/courses/661762/VBR_MP4h264_main_SD/661762_08_04_XR30_MonitoringAlerting.mp4?c3.ri=3774262273178924848&hashval=1576880099_83b1c764baa92bfd45ff8fcc30b6612c'




r = requests.get(url, stream=True)
with open("C:/Users/csb003/Documents/NCHpython/VideoDownload/lynda.mp4", "wb") as f:
    for chunk in r.iter_content(chunk_size = chunk_size):
        f.write(chunk)

