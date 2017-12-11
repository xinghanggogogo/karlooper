# -*-coding:utf-8-*-

"""

            #######################################################################
            #    _                     _                                          #
            #   | |                   | |                                         #
            #   | | __   __ _   _ __  | |   ___     ___    _ __     ___   _ __    #
            #   | |/ /  / _` | | '__| | |  / _ \   / _ \  | '_ \   / _ \ | '__|   #
            #   |   <  | (_| | | |    | | | (_) | | (_) | | |_) | |  __/ | |      #
            #   |_|\_\  \__,_| |_|    |_|  \___/   \___/  | .__/   \___| |_|      #
            #                                             | |                     #
            #                                             |_|                     #
            #                                                                     #
            #######################################################################

       _                            ___   _                     _  _           ___
    _ | |  ___   ___  _  _   ___   | _ ) | |  ___   ___  ___   | \| |  ___    | _ )  _  _   __ _
   | || | / -_) (_-< | || | (_-<   | _ \ | | / -_) (_-< (_-<   | .` | / _ \   | _ \ | || | / _` |
    \__/  \___| /__/  \_,_| /__/   |___/ |_| \___| /__/ /__/   |_|\_| \___/   |___/  \_,_| \__, |
                                                                                           |___/

"""

__author__ = 'karlvorndoenitz@gmail.com'
__version__ = '0.6.5'
__packages__ = [
    "autoreload",
    "config",
    "coroutine",
    "escape",
    "http_parser",
    "logger",
    "router",
    "template",
    "utils",
    "web"
]
VERSION = tuple(map(int, __version__.split('.')))
__logo__ = """


                                     .
                              .:tC0088880Gf;..
          ..18@@t.      ,t0@8Li.  . ...,,...:f0@8L:.  .,0808@i
          18i.  i@i.;G801,      .8@@888@@888@8:  .;C80f8:   .CG.
         :@: .Lf,t@0;.                ,@@.            :088@@G 0L
         :@: ;@@@f               f8@@@@@8@@88i          .L@@8 CC
          ,0@081.                     i@G.                .800G.
         .  00.                       i@G.                 .L0.
          :8t                   fCCLfttttttfCGC:            .L0.
         ;@;.                                                .LG
      . .81                                                   .0G
        GG.              .f0                        ;0i        ,8i
       .8;                .  .                  .L8L,           L0
       :@.                .;@@t                   ,Cf.          i8
       i@.                .1@8L.       :tti..     G@@f          18.
       :@Gt:.               .         ;@@@@8.      ::     .:f8@@@0
        8@@@@@@@8;                    . fG.               iG8800@1
        i8,..                     ..   .fL   iC             .,iG0
         L@888Gf1.                Cf...t8Gi;t8t .        ,8@@@@G.
          t@@@@8C,                 .:;.    .  .             :0L..
           .G8,                                           ;80.
             .L8L,                                    .iG8t.
               .,f08C;,.                       .,iL0808C.
                 ..Gf,iL0@@@888808000088888@@8Gfi,.   .GC
                  i8.  ,..                          i,..0f
                  G@Gi.8t               .   ..      i@,.08i
                 ;@t1::@;           i0@Gt1L@8i       G8GLC0.
                 L0;:,;8.         18t    .   t@i     18. :@1
                .8@@01t0.        0G.          ,8f    :8t@@@G
                ;@,  .GL        t0. .          ,8;   .@;  t8


"""
