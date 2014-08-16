from django import forms
import random
recap_dict = {  1 : 'jssfa',
                2 : 'wzajnf',
                3 : 'bstg',
                4 : 'ohnvc',
                5 : 'gckxqip',
                6 : 'reizlvx',
                7 : 'eedxgw',
                8 : 'hoyl',
                9 : 'bnpwa',
                10 : 'dmcqvo',
                11 : 'vmgnaam',
                12 : 'sdjhod',
                13 : 'hqtfr',
                14 : 'zpbsry',
                15 : 'doozezh',
                16 : 'nqajpdx',
                17 : 'toypf',
                18 : 'lkzfcb',
                19 : 'qhzgod',
                20 : 'gzinp',
                21 : 'dkssoyo',
                22 : 'vbhi',
                23 : 'jdsokbb',
                24 : 'epwbzbq',
                25 : 'liwhcm',
                26 : 'mtxl',
                27 : 'rhani',
                28 : 'sflvgc',
                29 : 'wmmcuyg',
                30 : 'mtpuq',
                31 : 'dunqr',
                32 : 'iittnsm',
                33 : 'wcjoou',
                34 : 'kvwp',
                35 : 'udmy',
                36 : 'vnfz',
                37 : 'yvtvorq',
                38 : 'hnle',
                39 : 'zmblhpo',
                40 : 'fawo',
                41 : 'vcvaz',
                42 : 'tbewjvb',
                43 : 'xxdbax',
                44 : 'luoucj',
                45 : 'rvfn',
                46 : 'fgbbf',
                47 : 'lhccq',
                48 : 'bvecq',
                49 : 'qovj',
                50 : 'scbkn',
                51 : 'xbmlq',
                52 : 'hgqcrru',
                53 : 'hvoap',
                54 : 'ahggv',
                55 : 'grgn',
                56 : 'ngrf',
                57 : 'tkionz',
                58 : 'gvybq',
                59 : 'ecyryw',
                60 : 'cjdffvs',
                61 : 'iwontwm',
                62 : 'omaqemb',
                63 : 'srgohn',
                64 : 'zsljx',
                65 : 'xzevt',
                66 : 'umgjj',
                67 : 'shrhjr',
                68 : 'wzrdtkc',
                69 : 'jwuyjr',
                70 : 'nwdbxdg',
                71 : 'rkvf',
                72 : 'hnphq',
                73 : 'mzufgse',
                74 : 'khjtj',
                75 : 'lyakhp',
                76 : 'rfhcgzt',
                77 : 'pevty',
                78 : 'flwjchc',
                79 : 'itpjf',
                80 : 'mcgvi',
                81 : 'dojojh',
                82 : 'dpzy',
                83 : 'haqp',
                84 : 'dtvwcpu',
                85 : 'floldvv',
                86 : 'gfzyhcx',
                87 : 'vjzucms',
                88 : 'kxte',
                89 : 'jtparr',
                90 : 'aymfvnx',
                91 : 'awirvn',
                92 : 'zacnhzn',
                93 : 'awihhm',
                94 : 'nynd',
                95 : 'syufqnz',
                96 : 'ljhdb',
                97 : 'lofvgg',
                98 : 'fggqh',
                99 : 'uwyr',
                100 : 'iwfj',
                101 : 'pkxk',
                102 : 'hgwaaxu',
                103 : 'bzzgbw',
                104 : 'lgao',
                105 : 'talpbwv',
                106 : 'pxlsewn',
                107 : 'lvrsgf',
                108 : 'fpsfjk',
                109 : 'rpdzhff',
                110 : 'urxke',
                111 : 'oyklzq',
                112 : 'yooz',
                113 : 'yhgce',
                114 : 'zkrfw',
                115 : 'nxecg',
                116 : 'nbaszb',
                117 : 'elwymbv',
                118 : 'yygkc',
                119 : 'svshfo',
                120 : 'avupnsi',
                121 : 'drbapcb',
                122 : 'hiql',
                123 : 'fbry',
                124 : 'ptrhgrf',
                125 : 'getcei',
                126 : 'ixtk',
                127 : 'dqzh',
                128 : 'apil',
                129 : 'yslpdb',
                130 : 'bbzvawo',
                131 : 'rorbkx',
                132 : 'duvl',
                133 : 'dptiv',
                134 : 'lgswqk',
                135 : 'ngiumzk',
                136 : 'hetdow',
                137 : 'oxtvyqx',
                138 : 'thahmtu',
                139 : 'jipxpo',
                140 : 'drzfj',
                141 : 'idit',
                142 : 'nwoyd',
                143 : 'fqyzqgt',
                144 : 'olipyd',
                145 : 'wjcazd',
                146 : 'jfykynq',
                147 : 'eiozru',
                148 : 'bkecxh',
                149 : 'yhfj',
                150 : 'wama',
                151 : 'njmexd',
                152 : 'dbmnlyd',
                153 : 'hhcfgqx',
                154 : 'ehlz',
                155 : 'pymnt',
                156 : 'xwou',
                157 : 'fuxyzsq',
                158 : 'fpcv',
                159 : 'yowo',
                160 : 'wzef',
                161 : 'ltyli',
                162 : 'dedv',
                163 : 'ajtw',
                164 : 'ukgjy',
                165 : 'igdlmyh',
                166 : 'fudlkz',
                167 : 'uwvni',
                168 : 'evhjpse',
                169 : 'ksfjxe',
                170 : 'ezkvyv',
                171 : 'zkjxwul',
                172 : 'swvusba',
                173 : 'mfmmp',
                174 : 'feylhjc',
                175 : 'puzfyrd',
                176 : 'yuzwptb',
                177 : 'tqghszw',
                178 : 'jolt',
                179 : 'cpfol',
                180 : 'lwza',
                181 : 'xgpuses',
                182 : 'fcisl',
                183 : 'ilgol',
                184 : 'zmnusl',
                185 : 'paak',
                186 : 'boowj',
                187 : 'quuolap',
                188 : 'kvzpftd',
                189 : 'xinocx',
                190 : 'wkcjsr',
                191 : 'nyexi',
                192 : 'wihvyif',
                193 : 'plfinq',
                194 : 'jgxpaf',
                195 : 'dngo',
                196 : 'jxjhizu',
                197 : 'biwujh',
                198 : 'tkjbrcg',
                199 : 'oduwlf',
                200 : 'hmvqur',
             }
'''
Creating custom fields? If the built-in Field classes don't meet your needs, you can 
easily create custom Field classes. To do this, just create a subclass of django.forms.Field. 
Its only requirements are that it implement a clean() method and that its __init__() method 
accept the core arguments mentioned above (required, label, initial, widget, help_text).
'''
class XRecahpWidget(forms.Widget):
    """
    Base class for all <input> widgets (except type='checkbox' and
    type='radio', which are special).
    """
    def render(self, name, value, attrs=None):           
        path, i = XVeifyHuman.get_image_path(); 
        html = "<img src=\"%s\" ></img>" % path
        html = html + "<div nowrap=\"nowrap\" class=\"muted\"><small>Please enter the the letters from above</small></div>"
        html = html + "<input type=\"text\" id=\"id_verify_human\" name=\"verify_human\"></input>";
        html = html + "<div style=\"display:none;\">   <input type=\"text\" id=\"id_verify_human_path\" name=\"verify_human_path\" value=\"%s\" ></input> </div>" % i;
        return html
        
    def value_from_datadict(self, data, files, name):
            return [data.get('verify_human', None), 
                    data.get('verify_human_path', None)]

class XRechapField(forms.Field):
    widget = XRecahpWidget 
    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
       super(XRechapField, self).__init__(*args, **kwargs)
  
    def clean(self, value):
        print "my clean_value is: " + str(value)
        if len(value) == 2:
                user_value = value[0]
                internal_id = value[1]    
                if     internal_id != '' and internal_id != None:       
                        internal_value = XVeifyHuman.get_image_value(internal_id)                        
                        if user_value != None and user_value != "":
                            if user_value == internal_value: 
                                return True
        raise forms.util.ValidationError("Please enter the word as shown ")
              
class XVeifyHuman(object):
    @staticmethod
    def get_image_value(image_id):
        value = recap_dict[int(image_id)]
        return value
  
    @staticmethod
    def get_image_path():
           i = random.randint(1, len(recap_dict.keys()))
           return "/a/static/default/img/recap/%d.jpg" % ( i ), i
           
    @staticmethod
    def gen_captcha(text, fnt, fnt_sz, file_name, fmt='JPEG'):
          import Image
          import ImageFont
          import ImageDraw
          import ImageFilter
  
          new_text = "";
          for i in range(0, len(text)):
              new_text = new_text + text[i] + " "
          text = new_text 
             
          """Generate a captcha image"""
          # randomly select the foreground color
          fgcolor = 0x999999 #random.randint(0,0xffff00)
          # make the background color the opposite of fgcolor
          bgcolor = 0xCCCCCC; #fgcolor ^ 0xffffff
          # create a font object 
          font = ImageFont.truetype(fnt,fnt_sz)
          # determine dimensions of the text
          dim = font.getsize(text)
          # create a new image slightly larger that the text
          im = Image.new('RGB', (dim[0]+0,dim[1]+0), bgcolor)
          d = ImageDraw.Draw(im)
          x, y = im.size
          r = random.randint
          # draw 100 random colored boxes on the background
          #for num in range(100):
          #  d.rectangle((r(0,x),r(0,y),r(0,x),r(0,y)),fill=r(0,0xffffff))
          # add the text to the image
          d.text((3,6), text, font=font, fill=fgcolor)
          im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
          # save the image to a file
          im.save(file_name, format=fmt)

    @staticmethod
    def write_captcha_list():
#        import string
#        for i in range(1,  201):
#              new_word = ""
#              for j in range(0, random.randint(4, 7)):
#                    new_word = new_word + str(random.choice(string.letters)).lower()
#              print "%s : '%s'," % (str(i), new_word)
              
        for key in recap_dict.keys():
            text = recap_dict[key] 
            fnt = "ARIAL.TTF"
            fnt_sz = 22
            file_name = "C:/xprj/xapp/htdocs/image/rechapcha\%s" % str(key) + ".jpg"
            XVeifyHuman.gen_captcha(text, fnt, fnt_sz, file_name, fmt='JPEG')