// License: GPLv3 Copyright: 2023, Kovid Goyal, <kovid at kovidgoyal.net>

package themes

import (
	"archive/zip"
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"io/fs"
	"maps"
	"net/http"
	"os"
	"path"
	"path/filepath"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"
	"time"

	"kitty/tools/cli"
	"kitty/tools/config"
	"kitty/tools/tui/loop"
	"kitty/tools/tui/subseq"
	"kitty/tools/utils"
	"kitty/tools/utils/style"
)

var _ = fmt.Print

var AllColorSettingNames = map[string]bool{ // {{{
	// generated by gen-config.py do not edit
	// ALL_COLORS_START
	"active_border_color":     true,
	"active_tab_background":   true,
	"active_tab_foreground":   true,
	"background":              true,
	"bell_border_color":       true,
	"color0":                  true,
	"color1":                  true,
	"color10":                 true,
	"color100":                true,
	"color101":                true,
	"color102":                true,
	"color103":                true,
	"color104":                true,
	"color105":                true,
	"color106":                true,
	"color107":                true,
	"color108":                true,
	"color109":                true,
	"color11":                 true,
	"color110":                true,
	"color111":                true,
	"color112":                true,
	"color113":                true,
	"color114":                true,
	"color115":                true,
	"color116":                true,
	"color117":                true,
	"color118":                true,
	"color119":                true,
	"color12":                 true,
	"color120":                true,
	"color121":                true,
	"color122":                true,
	"color123":                true,
	"color124":                true,
	"color125":                true,
	"color126":                true,
	"color127":                true,
	"color128":                true,
	"color129":                true,
	"color13":                 true,
	"color130":                true,
	"color131":                true,
	"color132":                true,
	"color133":                true,
	"color134":                true,
	"color135":                true,
	"color136":                true,
	"color137":                true,
	"color138":                true,
	"color139":                true,
	"color14":                 true,
	"color140":                true,
	"color141":                true,
	"color142":                true,
	"color143":                true,
	"color144":                true,
	"color145":                true,
	"color146":                true,
	"color147":                true,
	"color148":                true,
	"color149":                true,
	"color15":                 true,
	"color150":                true,
	"color151":                true,
	"color152":                true,
	"color153":                true,
	"color154":                true,
	"color155":                true,
	"color156":                true,
	"color157":                true,
	"color158":                true,
	"color159":                true,
	"color16":                 true,
	"color160":                true,
	"color161":                true,
	"color162":                true,
	"color163":                true,
	"color164":                true,
	"color165":                true,
	"color166":                true,
	"color167":                true,
	"color168":                true,
	"color169":                true,
	"color17":                 true,
	"color170":                true,
	"color171":                true,
	"color172":                true,
	"color173":                true,
	"color174":                true,
	"color175":                true,
	"color176":                true,
	"color177":                true,
	"color178":                true,
	"color179":                true,
	"color18":                 true,
	"color180":                true,
	"color181":                true,
	"color182":                true,
	"color183":                true,
	"color184":                true,
	"color185":                true,
	"color186":                true,
	"color187":                true,
	"color188":                true,
	"color189":                true,
	"color19":                 true,
	"color190":                true,
	"color191":                true,
	"color192":                true,
	"color193":                true,
	"color194":                true,
	"color195":                true,
	"color196":                true,
	"color197":                true,
	"color198":                true,
	"color199":                true,
	"color2":                  true,
	"color20":                 true,
	"color200":                true,
	"color201":                true,
	"color202":                true,
	"color203":                true,
	"color204":                true,
	"color205":                true,
	"color206":                true,
	"color207":                true,
	"color208":                true,
	"color209":                true,
	"color21":                 true,
	"color210":                true,
	"color211":                true,
	"color212":                true,
	"color213":                true,
	"color214":                true,
	"color215":                true,
	"color216":                true,
	"color217":                true,
	"color218":                true,
	"color219":                true,
	"color22":                 true,
	"color220":                true,
	"color221":                true,
	"color222":                true,
	"color223":                true,
	"color224":                true,
	"color225":                true,
	"color226":                true,
	"color227":                true,
	"color228":                true,
	"color229":                true,
	"color23":                 true,
	"color230":                true,
	"color231":                true,
	"color232":                true,
	"color233":                true,
	"color234":                true,
	"color235":                true,
	"color236":                true,
	"color237":                true,
	"color238":                true,
	"color239":                true,
	"color24":                 true,
	"color240":                true,
	"color241":                true,
	"color242":                true,
	"color243":                true,
	"color244":                true,
	"color245":                true,
	"color246":                true,
	"color247":                true,
	"color248":                true,
	"color249":                true,
	"color25":                 true,
	"color250":                true,
	"color251":                true,
	"color252":                true,
	"color253":                true,
	"color254":                true,
	"color255":                true,
	"color26":                 true,
	"color27":                 true,
	"color28":                 true,
	"color29":                 true,
	"color3":                  true,
	"color30":                 true,
	"color31":                 true,
	"color32":                 true,
	"color33":                 true,
	"color34":                 true,
	"color35":                 true,
	"color36":                 true,
	"color37":                 true,
	"color38":                 true,
	"color39":                 true,
	"color4":                  true,
	"color40":                 true,
	"color41":                 true,
	"color42":                 true,
	"color43":                 true,
	"color44":                 true,
	"color45":                 true,
	"color46":                 true,
	"color47":                 true,
	"color48":                 true,
	"color49":                 true,
	"color5":                  true,
	"color50":                 true,
	"color51":                 true,
	"color52":                 true,
	"color53":                 true,
	"color54":                 true,
	"color55":                 true,
	"color56":                 true,
	"color57":                 true,
	"color58":                 true,
	"color59":                 true,
	"color6":                  true,
	"color60":                 true,
	"color61":                 true,
	"color62":                 true,
	"color63":                 true,
	"color64":                 true,
	"color65":                 true,
	"color66":                 true,
	"color67":                 true,
	"color68":                 true,
	"color69":                 true,
	"color7":                  true,
	"color70":                 true,
	"color71":                 true,
	"color72":                 true,
	"color73":                 true,
	"color74":                 true,
	"color75":                 true,
	"color76":                 true,
	"color77":                 true,
	"color78":                 true,
	"color79":                 true,
	"color8":                  true,
	"color80":                 true,
	"color81":                 true,
	"color82":                 true,
	"color83":                 true,
	"color84":                 true,
	"color85":                 true,
	"color86":                 true,
	"color87":                 true,
	"color88":                 true,
	"color89":                 true,
	"color9":                  true,
	"color90":                 true,
	"color91":                 true,
	"color92":                 true,
	"color93":                 true,
	"color94":                 true,
	"color95":                 true,
	"color96":                 true,
	"color97":                 true,
	"color98":                 true,
	"color99":                 true,
	"cursor":                  true,
	"cursor_text_color":       true,
	"foreground":              true,
	"inactive_border_color":   true,
	"inactive_tab_background": true,
	"inactive_tab_foreground": true,
	"macos_titlebar_color":    true,
	"mark1_background":        true,
	"mark1_foreground":        true,
	"mark2_background":        true,
	"mark2_foreground":        true,
	"mark3_background":        true,
	"mark3_foreground":        true,
	"selection_background":    true,
	"selection_foreground":    true,
	"tab_bar_background":      true,
	"tab_bar_margin_color":    true,
	"url_color":               true,
	"visual_bell_color":       true,
	"wayland_titlebar_color":  true, // ALL_COLORS_END
} // }}}

type JSONMetadata struct {
	Etag      string `json:"etag"`
	Timestamp string `json:"timestamp"`
}

var ErrNoCacheFound = errors.New("No cache found and max cache age is negative")

func set_comment_in_zip_file(path string, comment string) error {
	src, err := zip.OpenReader(path)
	if err != nil {
		return err
	}
	defer src.Close()
	buf := bytes.Buffer{}
	dest := zip.NewWriter(&buf)
	if err = dest.SetComment(comment); err != nil {
		return err
	}
	for _, sf := range src.File {
		err = dest.Copy(sf)
		if err != nil {
			return err
		}
	}
	dest.Close()
	return utils.AtomicUpdateFile(path, buf.Bytes(), 0o644)
}

func fetch_cached(name, url, cache_path string, max_cache_age time.Duration) (string, error) {
	cache_path = filepath.Join(cache_path, name+".zip")
	zf, err := zip.OpenReader(cache_path)
	if err != nil && !errors.Is(err, fs.ErrNotExist) {
		return "", err
	}

	var jm JSONMetadata
	if err == nil {
		defer zf.Close()
		if err = json.Unmarshal(utils.UnsafeStringToBytes(zf.Comment), &jm); err == nil {
			if max_cache_age < 0 {
				return cache_path, nil
			}
			cache_age, err := utils.ISO8601Parse(jm.Timestamp)
			if err == nil {
				if time.Now().Before(cache_age.Add(max_cache_age)) {
					return cache_path, nil
				}
			}
		}
	}
	if max_cache_age < 0 {
		return "", ErrNoCacheFound
	}
	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		return "", err
	}
	if jm.Etag != "" {
		req.Header.Add("If-None-Match", jm.Etag)
	}
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("Failed to download %s with error: %w", url, err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		if resp.StatusCode == http.StatusNotModified {
			jm.Timestamp = utils.ISO8601Format(time.Now())
			comment, _ := json.Marshal(jm)
			err = set_comment_in_zip_file(cache_path, utils.UnsafeBytesToString(comment))
			if err != nil {
				return "", err
			}
			return cache_path, nil
		}
		return "", fmt.Errorf("Failed to download %s with HTTP error: %s", url, resp.Status)
	}
	var tf, tf2 *os.File
	tf, err = os.CreateTemp(filepath.Dir(cache_path), name+".temp-*")
	if err == nil {
		tf2, err = os.CreateTemp(filepath.Dir(cache_path), name+".temp-*")
	}
	defer func() {
		if tf != nil {
			tf.Close()
			os.Remove(tf.Name())
			tf = nil
		}
		if tf2 != nil {
			tf2.Close()
			os.Remove(tf2.Name())
			tf2 = nil
		}
	}()
	if err != nil {
		return "", fmt.Errorf("Failed to create temp file in %s with error: %w", filepath.Dir(cache_path), err)
	}
	_, err = io.Copy(tf, resp.Body)
	if err != nil {
		return "", fmt.Errorf("Failed to download %s with error: %w", url, err)
	}
	r, err := zip.OpenReader(tf.Name())
	if err != nil {
		return "", fmt.Errorf("Failed to open downloaded zip file with error: %w", err)
	}
	defer r.Close()
	w := zip.NewWriter(tf2)
	jm.Etag = resp.Header.Get("ETag")
	jm.Timestamp = utils.ISO8601Format(time.Now())
	comment, _ := json.Marshal(jm)
	if err = w.SetComment(utils.UnsafeBytesToString(comment)); err != nil {
		return "", err
	}
	for _, file := range r.File {
		err = w.Copy(file)
		if err != nil {
			return "", fmt.Errorf("Failed to copy zip file from source to destination archive")
		}
	}
	err = w.Close()
	if err != nil {
		return "", err
	}
	tf2.Close()
	err = os.Rename(tf2.Name(), cache_path)
	if err != nil {
		return "", fmt.Errorf("Failed to atomic rename temp file to %s with error: %w", cache_path, err)
	}
	tf2 = nil
	return cache_path, nil
}

func FetchCached(max_cache_age time.Duration) (string, error) {
	return fetch_cached("kitty-themes", "https://codeload.github.com/kovidgoyal/kitty-themes/zip/master", utils.CacheDir(), max_cache_age)
}

type ThemeMetadata struct {
	Name         string `json:"name"`
	Filepath     string `json:"file"`
	Is_dark      bool   `json:"is_dark"`
	Num_settings int    `json:"num_settings"`
	Blurb        string `json:"blurb"`
	License      string `json:"license"`
	Upstream     string `json:"upstream"`
	Author       string `json:"author"`
}

func ParseThemeMetadata(path string) (*ThemeMetadata, map[string]string, error) {
	var in_metadata, in_blurb, finished_metadata bool
	ans := ThemeMetadata{Is_dark: true} // the default background in kitty is dark
	settings := map[string]string{}

	read_is_dark := func(key, val string) (err error) {
		settings[key] = val
		if key == "background" {
			if val != "" {
				bg, err := style.ParseColor(val)
				if err == nil {
					ans.Is_dark = utils.Max(bg.Red, bg.Green, bg.Blue) < 115
				}
			}
		}
		return
	}
	read_metadata := func(line string) (err error) {
		is_block := strings.HasPrefix(line, "## ")
		if in_metadata && !is_block {
			finished_metadata = true
		}
		if finished_metadata {
			return
		}
		if !in_metadata && is_block {
			in_metadata = true
		}
		if !in_metadata {
			return
		}
		line = line[3:]
		if in_blurb {
			ans.Blurb += " " + line
			return
		}
		key, val, found := strings.Cut(line, ":")
		if !found {
			return
		}
		key = strings.TrimSpace(strings.ToLower(key))
		val = strings.TrimSpace(val)
		switch key {
		case "name":
			if val != "The name of the theme (if not present, derived from filename)" {
				ans.Name = val
			}
		case "author":
			ans.Author = val
		case "upstream":
			ans.Upstream = val
		case "blurb":
			ans.Blurb = val
			in_blurb = true
		case "license":
			ans.License = val
		}
		return
	}
	cp := config.ConfigParser{LineHandler: read_is_dark, CommentsHandler: read_metadata}
	err := cp.ParseFiles(path)
	if err != nil {
		return nil, nil, err
	}
	ans.Num_settings = len(settings)
	return &ans, settings, nil
}

type Theme struct {
	metadata *ThemeMetadata

	code                        string
	settings                    map[string]string
	zip_reader                  *zip.File
	is_user_defined             bool
	path_for_user_defined_theme string
}

func (self *Theme) Name() string        { return self.metadata.Name }
func (self *Theme) Author() string      { return self.metadata.Author }
func (self *Theme) Blurb() string       { return self.metadata.Blurb }
func (self *Theme) IsDark() bool        { return self.metadata.Is_dark }
func (self *Theme) IsUserDefined() bool { return self.is_user_defined }

func (self *Theme) load_code() (string, error) {
	if self.zip_reader != nil {
		f, err := self.zip_reader.Open()
		self.zip_reader = nil
		if err != nil {
			return "", err
		}
		defer f.Close()
		data, err := io.ReadAll(f)
		if err != nil {
			return "", err
		}
		self.code = utils.UnsafeBytesToString(data)
	}
	if self.is_user_defined && self.path_for_user_defined_theme != "" && self.code == "" {
		raw, err := os.ReadFile(self.path_for_user_defined_theme)
		if err != nil {
			return "", err
		}
		self.code = utils.UnsafeBytesToString(raw)
	}
	return self.code, nil
}

func (self *Theme) Code() (string, error) {
	return self.load_code()
}

func (self *Theme) SaveInDir(dirpath string) (err error) {
	path := filepath.Join(dirpath, self.Name()+".conf")
	code, err := self.Code()
	if err != nil {
		return err
	}
	return utils.AtomicUpdateFile(path, utils.UnsafeStringToBytes(code), 0o644)
}

func (self *Theme) SaveInConf(config_dir, reload_in, config_file_name string) (err error) {
	_ = os.MkdirAll(config_dir, 0o755)
	path := filepath.Join(config_dir, `current-theme.conf`)
	code, err := self.Code()
	if err != nil {
		return err
	}
	err = utils.AtomicUpdateFile(path, utils.UnsafeStringToBytes(code), 0o644)
	if err != nil {
		return err
	}
	confpath := config_file_name
	if !filepath.IsAbs(config_file_name) {
		confpath = filepath.Join(config_dir, config_file_name)
	}
	patcher := config.Patcher{Write_backup: true}
	if _, err = patcher.Patch(
		confpath, "KITTY_THEME", fmt.Sprintf("# %s\ninclude current-theme.conf", self.metadata.Name),
		utils.Keys(AllColorSettingNames)...); err != nil {
		return
	}
	switch reload_in {
	case "parent":
		config.ReloadConfigInKitty(true)
	case "all":
		config.ReloadConfigInKitty(false)
	}
	return
}

func (self *Theme) Settings() (map[string]string, error) {
	if self.zip_reader != nil {
		code, err := self.load_code()
		if err != nil {
			return nil, err
		}
		self.settings = make(map[string]string, 64)
		scanner := utils.NewLineScanner(code)
		for scanner.Scan() {
			line := strings.TrimSpace(scanner.Text())
			if line != "" && line[0] != '#' {
				key, val, found := strings.Cut(line, " ")
				if found {
					self.settings[key] = val
				}
			}
		}
	}
	return self.settings, nil
}

func (self *Theme) AsEscapeCodes() (string, error) {
	settings, err := self.Settings()
	if err != nil {
		return "", err
	}
	return ColorSettingsAsEscapeCodes(settings), nil
}

func ColorSettingsAsEscapeCodes(settings map[string]string) string {
	w := strings.Builder{}
	w.Grow(4096)

	set_color := func(i int, sharp string) {
		w.WriteByte(';')
		w.WriteString(strconv.Itoa(i))
		w.WriteByte(';')
		w.WriteString(sharp)
	}

	set_default_color := func(name, defval string, num loop.DefaultColor) {
		w.WriteString("\033]")
		defer func() { w.WriteString("\033\\") }()
		val, found := settings[name]
		if !found {
			val = defval
		}
		if val != "" {
			rgba, err := style.ParseColor(val)
			if err == nil {
				w.WriteString(strconv.Itoa(int(num)))
				w.WriteByte(';')
				w.WriteString(rgba.AsRGBSharp())
				return
			}
		}
		w.WriteByte('1')
		w.WriteString(strconv.Itoa(int(num)))
	}
	set_default_color("foreground", style.DefaultColors.Foreground, loop.FOREGROUND)
	set_default_color("background", style.DefaultColors.Background, loop.BACKGROUND)
	set_default_color("cursor", style.DefaultColors.Cursor, loop.CURSOR)
	set_default_color("selection_background", style.DefaultColors.SelectionBg, loop.SELECTION_BG)
	set_default_color("selection_foreground", style.DefaultColors.SelectionFg, loop.SELECTION_FG)

	w.WriteString("\033]4")
	for i := 0; i < 256; i++ {
		key := "color" + strconv.Itoa(i)
		val := settings[key]
		if val != "" {
			rgba, err := style.ParseColor(val)
			if err == nil {
				set_color(i, rgba.AsRGBSharp())
				continue
			}
		}
		rgba := style.RGBA{}
		rgba.FromRGB(style.ColorTable[i])
		set_color(i, rgba.AsRGBSharp())
	}
	w.WriteString("\033\\")
	return w.String()
}

type Themes struct {
	name_map  map[string]*Theme
	index_map []string
}

func (self *Themes) Copy() *Themes {
	ans := &Themes{name_map: make(map[string]*Theme, len(self.name_map)), index_map: slices.Clone(self.index_map)}
	maps.Copy(ans.name_map, self.name_map)
	return ans
}

var camel_case_pat = sync.OnceValue(func() *regexp.Regexp {
	return regexp.MustCompile(`([a-z])([A-Z])`)
})

func ThemeNameFromFileName(fname string) string {
	fname = fname[:len(fname)-len(path.Ext(fname))]
	fname = strings.ReplaceAll(fname, "_", " ")
	fname = camel_case_pat().ReplaceAllString(fname, "$1 $2")
	return strings.Join(utils.Map(strings.Title, strings.Split(fname, " ")), " ")
}

func (self *Themes) Len() int { return len(self.name_map) }
func (self *Themes) At(x int) *Theme {
	if x >= len(self.index_map) || x < 0 {
		return nil
	}
	return self.name_map[self.index_map[x]]
}
func (self *Themes) Names() []string { return self.index_map }

func (self *Themes) create_index_map() {
	self.index_map = utils.Keys(self.name_map)
	self.index_map = utils.StableSortWithKey(self.index_map, strings.ToLower)
}

func (self *Themes) Filtered(is_ok func(*Theme) bool) *Themes {
	themes := utils.Filter(utils.Values(self.name_map), is_ok)
	ans := Themes{name_map: make(map[string]*Theme, len(themes))}
	for _, theme := range themes {
		ans.name_map[theme.metadata.Name] = theme
	}
	ans.create_index_map()
	return &ans
}

func (self *Themes) AddFromFile(path string) (*Theme, error) {
	m, conf, err := ParseThemeMetadata(path)
	if err != nil {
		return nil, err
	}
	if m.Name == "" {
		m.Name = ThemeNameFromFileName(filepath.Base(path))
	}
	t := Theme{metadata: m, is_user_defined: true, settings: conf, path_for_user_defined_theme: path}
	self.name_map[m.Name] = &t
	return &t, nil

}

func (self *Themes) add_from_dir(dirpath string) error {
	entries, err := os.ReadDir(dirpath)
	if err != nil {
		if errors.Is(err, fs.ErrNotExist) {
			err = nil
		}
		return err
	}
	for _, e := range entries {
		if !e.IsDir() && strings.HasSuffix(e.Name(), ".conf") {
			path := filepath.Join(dirpath, e.Name())
			// ignore files if they are the STDOUT of the current processes
			// allows using kitten theme --dump-theme name > ~/.config/kitty/themes/name.conf
			if utils.Samefile(path, os.Stdout) {
				continue
			}
			if _, err = self.AddFromFile(path); err != nil {
				return err
			}
		}
	}
	return nil
}

func (self *Themes) add_from_zip_file(zippath string) (io.Closer, error) {
	r, err := zip.OpenReader(zippath)
	if err != nil {
		return nil, err
	}
	name_map := make(map[string]*zip.File, len(r.File))
	var themes []*ThemeMetadata
	theme_dir := ""
	for _, file := range r.File {
		name_map[file.Name] = file
		if path.Base(file.Name) == "themes.json" {
			theme_dir = path.Dir(file.Name)
			fr, err := file.Open()
			if err != nil {
				return nil, fmt.Errorf("Error while opening %s from the ZIP file: %w", file.Name, err)
			}
			defer fr.Close()
			raw, err := io.ReadAll(fr)
			if err != nil {
				return nil, fmt.Errorf("Error while reading %s from the ZIP file: %w", file.Name, err)
			}
			err = json.Unmarshal(raw, &themes)
			if err != nil {
				return nil, fmt.Errorf("Error while decoding %s: %w", file.Name, err)
			}
		}
	}
	if theme_dir == "" {
		return nil, fmt.Errorf("No themes.json found in ZIP file")
	}
	for _, theme := range themes {
		key := path.Join(theme_dir, theme.Filepath)
		f := name_map[key]
		if f != nil {
			t := Theme{metadata: theme, zip_reader: f}
			self.name_map[theme.Name] = &t
		}
	}
	return r, nil
}

func (self *Themes) ThemeByName(name string) *Theme {
	ans := self.name_map[name]
	if ans == nil {
		q := strings.ToLower(name)
		for k, t := range self.name_map {
			if strings.ToLower(k) == q {
				return t
			}
		}
	}
	return ans
}

func match(expression string, items []string) []*subseq.Match {
	matches := subseq.ScoreItems(expression, items, subseq.Options{Level1: " "})
	matches = utils.StableSort(matches, func(a, b *subseq.Match) int {
		if b.Score < a.Score {
			return -1
		}
		if b.Score > a.Score {
			return 1
		}
		return 0
	})
	return matches
}

const (
	MARK_BEFORE = "\033[33m"
	MARK_AFTER  = "\033[39m"
)

func (self *Themes) ApplySearch(expression string, marks ...string) []string {
	mark_before, mark_after := MARK_BEFORE, MARK_AFTER
	if len(marks) == 2 {
		mark_before, mark_after = marks[0], marks[1]
	}
	results := utils.Filter(match(expression, self.index_map), func(x *subseq.Match) bool { return x.Score > 0 })
	name_map := make(map[string]*Theme, len(results))
	for _, m := range results {
		name_map[m.Text] = self.name_map[m.Text]
	}
	self.name_map = name_map
	self.index_map = self.index_map[:0]
	ans := make([]string, 0, len(results))
	for _, m := range results {
		text := m.Text
		positions := m.Positions
		for i := len(positions) - 1; i >= 0; i-- {
			p := positions[i]
			text = text[:p] + mark_before + text[p:p+1] + mark_after + text[p+1:]
		}
		ans = append(ans, text)
		self.index_map = append(self.index_map, m.Text)
	}
	return ans
}

func LoadThemes(cache_age time.Duration) (ans *Themes, closer io.Closer, err error) {
	zip_path, err := FetchCached(cache_age)
	ans = &Themes{name_map: make(map[string]*Theme)}
	if err != nil {
		return nil, nil, err
	}
	if closer, err = ans.add_from_zip_file(zip_path); err != nil {
		return nil, nil, err
	}
	if err = ans.add_from_dir(filepath.Join(utils.ConfigDir(), "themes")); err != nil {
		return nil, nil, err
	}
	ans.create_index_map()
	return ans, closer, nil
}

func ThemeFromFile(path string) (*Theme, error) {
	ans := &Themes{name_map: make(map[string]*Theme)}
	return ans.AddFromFile(path)
}

func GetThemeNames(cache_age time.Duration) (ans []string, err error) {
	themes, closer, err := LoadThemes(cache_age)
	if err != nil {
		if errors.Is(err, ErrNoCacheFound) {
			return []string{"Default"}, nil
		}
		return nil, err
	}
	defer closer.Close()
	for name := range themes.name_map {
		ans = append(ans, name)
	}
	return
}

func CompleteThemes(completions *cli.Completions, word string, arg_num int) {
	names, err := GetThemeNames(-1)
	if err == nil {
		mg := completions.AddMatchGroup("Themes")
		for _, theme_name := range names {
			theme_name = strings.TrimSpace(theme_name)
			if theme_name != "" && strings.HasPrefix(theme_name, word) {
				mg.AddMatch(theme_name)
			}
		}
	}
}
