# generated by gen-config.py DO NOT edit

import typing
from array import array
from kitty.constants import is_macos
import kitty.constants
from kitty.fast_data_types import Color
import kitty.fast_data_types
from kitty.options.utils import AliasMap, KeyDefinition, KeyMap, MouseMap, MouseMapping, SequenceMap, TabBarMarginHeight
import kitty.options.utils
from kitty.types import FloatEdges, SingleKey
import kitty.types

if typing.TYPE_CHECKING:
    choices_for_background_image_layout = typing.Literal['mirror-tiled', 'scaled', 'tiled', 'clamped']
    choices_for_default_pointer_shape = typing.Literal['arrow', 'beam', 'hand']
    choices_for_linux_display_server = typing.Literal['auto', 'wayland', 'x11']
    choices_for_macos_show_window_title_in = typing.Literal['all', 'menubar', 'none', 'window']
    choices_for_placement_strategy = typing.Literal['center', 'top-left']
    choices_for_pointer_shape_when_dragging = typing.Literal['arrow', 'beam', 'hand']
    choices_for_pointer_shape_when_grabbed = typing.Literal['arrow', 'beam', 'hand']
    choices_for_strip_trailing_spaces = typing.Literal['always', 'never', 'smart']
    choices_for_tab_bar_align = typing.Literal['left', 'center', 'right']
    choices_for_tab_bar_style = typing.Literal['fade', 'hidden', 'powerline', 'separator', 'slant', 'custom']
    choices_for_tab_powerline_style = typing.Literal['angled', 'round', 'slanted']
    choices_for_tab_switch_strategy = typing.Literal['last', 'left', 'previous', 'right']
    choices_for_window_logo_position = typing.Literal['top-left', 'top', 'top-right', 'left', 'center', 'right', 'bottom-left', 'bottom', 'bottom-right']
else:
    choices_for_background_image_layout = str
    choices_for_default_pointer_shape = str
    choices_for_linux_display_server = str
    choices_for_macos_show_window_title_in = str
    choices_for_placement_strategy = str
    choices_for_pointer_shape_when_dragging = str
    choices_for_pointer_shape_when_grabbed = str
    choices_for_strip_trailing_spaces = str
    choices_for_tab_bar_align = str
    choices_for_tab_bar_style = str
    choices_for_tab_powerline_style = str
    choices_for_tab_switch_strategy = str
    choices_for_window_logo_position = str

option_names = (  # {{{
 'action_alias',
 'active_border_color',
 'active_tab_background',
 'active_tab_font_style',
 'active_tab_foreground',
 'active_tab_title_template',
 'adjust_baseline',
 'adjust_column_width',
 'adjust_line_height',
 'allow_hyperlinks',
 'allow_remote_control',
 'background',
 'background_image',
 'background_image_layout',
 'background_image_linear',
 'background_opacity',
 'background_tint',
 'bell_border_color',
 'bell_on_tab',
 'bell_path',
 'bold_font',
 'bold_italic_font',
 'box_drawing_scale',
 'clear_all_mouse_actions',
 'clear_all_shortcuts',
 'click_interval',
 'clipboard_control',
 'clipboard_max_size',
 'close_on_child_death',
 'color0',
 'color1',
 'color2',
 'color3',
 'color4',
 'color5',
 'color6',
 'color7',
 'color8',
 'color9',
 'color10',
 'color11',
 'color12',
 'color13',
 'color14',
 'color15',
 'color16',
 'color17',
 'color18',
 'color19',
 'color20',
 'color21',
 'color22',
 'color23',
 'color24',
 'color25',
 'color26',
 'color27',
 'color28',
 'color29',
 'color30',
 'color31',
 'color32',
 'color33',
 'color34',
 'color35',
 'color36',
 'color37',
 'color38',
 'color39',
 'color40',
 'color41',
 'color42',
 'color43',
 'color44',
 'color45',
 'color46',
 'color47',
 'color48',
 'color49',
 'color50',
 'color51',
 'color52',
 'color53',
 'color54',
 'color55',
 'color56',
 'color57',
 'color58',
 'color59',
 'color60',
 'color61',
 'color62',
 'color63',
 'color64',
 'color65',
 'color66',
 'color67',
 'color68',
 'color69',
 'color70',
 'color71',
 'color72',
 'color73',
 'color74',
 'color75',
 'color76',
 'color77',
 'color78',
 'color79',
 'color80',
 'color81',
 'color82',
 'color83',
 'color84',
 'color85',
 'color86',
 'color87',
 'color88',
 'color89',
 'color90',
 'color91',
 'color92',
 'color93',
 'color94',
 'color95',
 'color96',
 'color97',
 'color98',
 'color99',
 'color100',
 'color101',
 'color102',
 'color103',
 'color104',
 'color105',
 'color106',
 'color107',
 'color108',
 'color109',
 'color110',
 'color111',
 'color112',
 'color113',
 'color114',
 'color115',
 'color116',
 'color117',
 'color118',
 'color119',
 'color120',
 'color121',
 'color122',
 'color123',
 'color124',
 'color125',
 'color126',
 'color127',
 'color128',
 'color129',
 'color130',
 'color131',
 'color132',
 'color133',
 'color134',
 'color135',
 'color136',
 'color137',
 'color138',
 'color139',
 'color140',
 'color141',
 'color142',
 'color143',
 'color144',
 'color145',
 'color146',
 'color147',
 'color148',
 'color149',
 'color150',
 'color151',
 'color152',
 'color153',
 'color154',
 'color155',
 'color156',
 'color157',
 'color158',
 'color159',
 'color160',
 'color161',
 'color162',
 'color163',
 'color164',
 'color165',
 'color166',
 'color167',
 'color168',
 'color169',
 'color170',
 'color171',
 'color172',
 'color173',
 'color174',
 'color175',
 'color176',
 'color177',
 'color178',
 'color179',
 'color180',
 'color181',
 'color182',
 'color183',
 'color184',
 'color185',
 'color186',
 'color187',
 'color188',
 'color189',
 'color190',
 'color191',
 'color192',
 'color193',
 'color194',
 'color195',
 'color196',
 'color197',
 'color198',
 'color199',
 'color200',
 'color201',
 'color202',
 'color203',
 'color204',
 'color205',
 'color206',
 'color207',
 'color208',
 'color209',
 'color210',
 'color211',
 'color212',
 'color213',
 'color214',
 'color215',
 'color216',
 'color217',
 'color218',
 'color219',
 'color220',
 'color221',
 'color222',
 'color223',
 'color224',
 'color225',
 'color226',
 'color227',
 'color228',
 'color229',
 'color230',
 'color231',
 'color232',
 'color233',
 'color234',
 'color235',
 'color236',
 'color237',
 'color238',
 'color239',
 'color240',
 'color241',
 'color242',
 'color243',
 'color244',
 'color245',
 'color246',
 'color247',
 'color248',
 'color249',
 'color250',
 'color251',
 'color252',
 'color253',
 'color254',
 'color255',
 'command_on_bell',
 'confirm_os_window_close',
 'copy_on_select',
 'cursor',
 'cursor_beam_thickness',
 'cursor_blink_interval',
 'cursor_shape',
 'cursor_stop_blinking_after',
 'cursor_text_color',
 'cursor_underline_thickness',
 'default_pointer_shape',
 'detect_urls',
 'dim_opacity',
 'disable_ligatures',
 'draw_minimal_borders',
 'dynamic_background_opacity',
 'editor',
 'enable_audio_bell',
 'enabled_layouts',
 'env',
 'exe_search_path',
 'file_transfer_confirmation_bypass',
 'focus_follows_mouse',
 'font_family',
 'font_features',
 'font_size',
 'force_ltr',
 'foreground',
 'hide_window_decorations',
 'inactive_border_color',
 'inactive_tab_background',
 'inactive_tab_font_style',
 'inactive_tab_foreground',
 'inactive_text_alpha',
 'initial_window_height',
 'initial_window_width',
 'input_delay',
 'italic_font',
 'kitten_alias',
 'kitty_mod',
 'linux_display_server',
 'listen_on',
 'macos_custom_beam_cursor',
 'macos_hide_from_tasks',
 'macos_option_as_alt',
 'macos_quit_when_last_window_closed',
 'macos_show_window_title_in',
 'macos_thicken_font',
 'macos_titlebar_color',
 'macos_traditional_fullscreen',
 'macos_window_resizable',
 'map',
 'mark1_background',
 'mark1_foreground',
 'mark2_background',
 'mark2_foreground',
 'mark3_background',
 'mark3_foreground',
 'mouse_hide_wait',
 'mouse_map',
 'open_url_with',
 'placement_strategy',
 'pointer_shape_when_dragging',
 'pointer_shape_when_grabbed',
 'remember_window_size',
 'repaint_delay',
 'resize_debounce_time',
 'resize_draw_strategy',
 'resize_in_steps',
 'scrollback_fill_enlarged_window',
 'scrollback_lines',
 'scrollback_pager',
 'scrollback_pager_history_size',
 'select_by_word_characters',
 'selection_background',
 'selection_foreground',
 'shell',
 'shell_integration',
 'single_window_margin_width',
 'startup_session',
 'strip_trailing_spaces',
 'symbol_map',
 'sync_to_monitor',
 'tab_activity_symbol',
 'tab_bar_align',
 'tab_bar_background',
 'tab_bar_edge',
 'tab_bar_margin_color',
 'tab_bar_margin_height',
 'tab_bar_margin_width',
 'tab_bar_min_tabs',
 'tab_bar_style',
 'tab_fade',
 'tab_powerline_style',
 'tab_separator',
 'tab_switch_strategy',
 'tab_title_template',
 'term',
 'touch_scroll_multiplier',
 'update_check_interval',
 'url_color',
 'url_excluded_characters',
 'url_prefixes',
 'url_style',
 'visual_bell_color',
 'visual_bell_duration',
 'visual_window_select_characters',
 'watcher',
 'wayland_titlebar_color',
 'wheel_scroll_multiplier',
 'window_alert_on_bell',
 'window_border_width',
 'window_logo_alpha',
 'window_logo_path',
 'window_logo_position',
 'window_margin_width',
 'window_padding_width',
 'window_resize_step_cells',
 'window_resize_step_lines')  # }}}


class Options:
    active_border_color: typing.Optional[kitty.fast_data_types.Color] = Color(0, 255, 0)
    active_tab_background: Color = Color(238, 238, 238)
    active_tab_font_style: typing.Tuple[bool, bool] = (True, True)
    active_tab_foreground: Color = Color(0, 0, 0)
    active_tab_title_template: typing.Optional[str] = None
    adjust_baseline: typing.Union[int, float] = 0
    adjust_column_width: typing.Union[int, float] = 0
    adjust_line_height: typing.Union[int, float] = 0
    allow_hyperlinks: int = 1
    allow_remote_control: str = 'n'
    background: Color = Color(0, 0, 0)
    background_image: typing.Optional[str] = None
    background_image_layout: choices_for_background_image_layout = 'tiled'
    background_image_linear: bool = False
    background_opacity: float = 1.0
    background_tint: float = 0
    bell_border_color: Color = Color(255, 90, 0)
    bell_on_tab: bool = True
    bell_path: typing.Optional[str] = None
    bold_font: str = 'auto'
    bold_italic_font: str = 'auto'
    box_drawing_scale: typing.Tuple[float, float, float, float] = (0.001, 1.0, 1.5, 2.0)
    clear_all_mouse_actions: bool = False
    clear_all_shortcuts: bool = False
    click_interval: float = -1.0
    clipboard_control: typing.Tuple[str, ...] = ('write-clipboard', 'write-primary', 'read-clipboard-ask', 'read-primary-ask')
    clipboard_max_size: float = 64.0
    close_on_child_death: bool = False
    command_on_bell: typing.List[str] = ['none']
    confirm_os_window_close: int = 0
    copy_on_select: str = ''
    cursor: typing.Optional[kitty.fast_data_types.Color] = Color(204, 204, 204)
    cursor_beam_thickness: float = 1.5
    cursor_blink_interval: float = -1.0
    cursor_shape: int = 1
    cursor_stop_blinking_after: float = 15.0
    cursor_text_color: typing.Optional[kitty.fast_data_types.Color] = Color(17, 17, 17)
    cursor_underline_thickness: float = 2.0
    default_pointer_shape: choices_for_default_pointer_shape = 'beam'
    detect_urls: bool = True
    dim_opacity: float = 0.75
    disable_ligatures: int = 0
    draw_minimal_borders: bool = True
    dynamic_background_opacity: bool = False
    editor: str = '.'
    enable_audio_bell: bool = True
    enabled_layouts: typing.List[str] = ['fat', 'grid', 'horizontal', 'splits', 'stack', 'tall', 'vertical']
    file_transfer_confirmation_bypass: str = ''
    focus_follows_mouse: bool = False
    font_family: str = 'monospace'
    font_size: float = 11.0
    force_ltr: bool = False
    foreground: Color = Color(221, 221, 221)
    hide_window_decorations: int = 0
    inactive_border_color: Color = Color(204, 204, 204)
    inactive_tab_background: Color = Color(153, 153, 153)
    inactive_tab_font_style: typing.Tuple[bool, bool] = (False, False)
    inactive_tab_foreground: Color = Color(68, 68, 68)
    inactive_text_alpha: float = 1.0
    initial_window_height: typing.Tuple[int, str] = (400, 'px')
    initial_window_width: typing.Tuple[int, str] = (640, 'px')
    input_delay: int = 3
    italic_font: str = 'auto'
    kitty_mod: int = 5
    linux_display_server: choices_for_linux_display_server = 'auto'
    listen_on: str = 'none'
    macos_custom_beam_cursor: bool = False
    macos_hide_from_tasks: bool = False
    macos_option_as_alt: int = 0
    macos_quit_when_last_window_closed: bool = False
    macos_show_window_title_in: choices_for_macos_show_window_title_in = 'all'
    macos_thicken_font: float = 0
    macos_titlebar_color: int = 0
    macos_traditional_fullscreen: bool = False
    macos_window_resizable: bool = True
    mark1_background: Color = Color(152, 211, 203)
    mark1_foreground: Color = Color(0, 0, 0)
    mark2_background: Color = Color(242, 220, 211)
    mark2_foreground: Color = Color(0, 0, 0)
    mark3_background: Color = Color(242, 116, 188)
    mark3_foreground: Color = Color(0, 0, 0)
    mouse_hide_wait: float = 0.0 if is_macos else 3.0
    open_url_with: typing.List[str] = ['default']
    placement_strategy: choices_for_placement_strategy = 'center'
    pointer_shape_when_dragging: choices_for_pointer_shape_when_dragging = 'beam'
    pointer_shape_when_grabbed: choices_for_pointer_shape_when_grabbed = 'arrow'
    remember_window_size: bool = True
    repaint_delay: int = 10
    resize_debounce_time: float = 0.1
    resize_draw_strategy: int = 0
    resize_in_steps: bool = False
    scrollback_fill_enlarged_window: bool = False
    scrollback_lines: int = 2000
    scrollback_pager: typing.List[str] = ['less', '--chop-long-lines', '--RAW-CONTROL-CHARS', '+INPUT_LINE_NUMBER']
    scrollback_pager_history_size: int = 0
    select_by_word_characters: str = '@-./_~?&=%+#'
    selection_background: typing.Optional[kitty.fast_data_types.Color] = Color(255, 250, 205)
    selection_foreground: typing.Optional[kitty.fast_data_types.Color] = Color(0, 0, 0)
    shell: str = '.'
    shell_integration: typing.FrozenSet[str] = frozenset({'enabled'})
    single_window_margin_width: FloatEdges = FloatEdges(left=-1.0, top=-1.0, right=-1.0, bottom=-1.0)
    startup_session: typing.Optional[str] = None
    strip_trailing_spaces: choices_for_strip_trailing_spaces = 'never'
    sync_to_monitor: bool = True
    tab_activity_symbol: typing.Optional[str] = None
    tab_bar_align: choices_for_tab_bar_align = 'left'
    tab_bar_background: typing.Optional[kitty.fast_data_types.Color] = None
    tab_bar_edge: int = 3
    tab_bar_margin_color: typing.Optional[kitty.fast_data_types.Color] = None
    tab_bar_margin_height: TabBarMarginHeight = TabBarMarginHeight(outer=0, inner=0)
    tab_bar_margin_width: float = 0
    tab_bar_min_tabs: int = 2
    tab_bar_style: choices_for_tab_bar_style = 'fade'
    tab_fade: typing.Tuple[float, ...] = (0.25, 0.5, 0.75, 1.0)
    tab_powerline_style: choices_for_tab_powerline_style = 'angled'
    tab_separator: str = ' ┇'
    tab_switch_strategy: choices_for_tab_switch_strategy = 'previous'
    tab_title_template: str = '{title}'
    term: str = 'xterm-kitty'
    touch_scroll_multiplier: float = 1.0
    update_check_interval: float = 24.0
    url_color: Color = Color(0, 135, 189)
    url_excluded_characters: str = ''
    url_prefixes: typing.Tuple[str, ...] = ('http', 'https', 'file', 'ftp', 'gemini', 'irc', 'gopher', 'mailto', 'news', 'git')
    url_style: int = 3
    visual_bell_color: typing.Optional[kitty.fast_data_types.Color] = None
    visual_bell_duration: float = 0
    visual_window_select_characters: str = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wayland_titlebar_color: int = 0
    wheel_scroll_multiplier: float = 5.0
    window_alert_on_bell: bool = True
    window_border_width: typing.Tuple[float, str] = (0.5, 'pt')
    window_logo_alpha: float = 0.5
    window_logo_path: typing.Optional[str] = None
    window_logo_position: choices_for_window_logo_position = 'bottom-right'
    window_margin_width: FloatEdges = FloatEdges(left=0, top=0, right=0, bottom=0)
    window_padding_width: FloatEdges = FloatEdges(left=0, top=0, right=0, bottom=0)
    window_resize_step_cells: int = 2
    window_resize_step_lines: int = 2
    action_alias: typing.Dict[str, str] = {}
    env: typing.Dict[str, str] = {}
    exe_search_path: typing.Dict[str, str] = {}
    font_features: typing.Dict[str, typing.Tuple[kitty.fonts.FontFeature, ...]] = {}
    kitten_alias: typing.Dict[str, str] = {}
    symbol_map: typing.Dict[typing.Tuple[int, int], str] = {}
    watcher: typing.Dict[str, str] = {}
    map: typing.List[kitty.options.utils.KeyDefinition] = []
    keymap: KeyMap = {}
    sequence_map: SequenceMap = {}
    alias_map: AliasMap = AliasMap()
    mouse_map: typing.List[kitty.options.utils.MouseMapping] = []
    mousemap: MouseMap = {}
    color_table: "array[int]" = array("L", (
        0x000000, 0xcc0403, 0x19cb00, 0xcecb00, 0x0d73cc, 0xcb1ed1, 0x0dcdcd, 0xdddddd,
        0x767676, 0xf2201f, 0x23fd00, 0xfffd00, 0x1a8fff, 0xfd28ff, 0x14ffff, 0xffffff,
        0x000000, 0x00005f, 0x000087, 0x0000af, 0x0000d7, 0x0000ff, 0x005f00, 0x005f5f,
        0x005f87, 0x005faf, 0x005fd7, 0x005fff, 0x008700, 0x00875f, 0x008787, 0x0087af,
        0x0087d7, 0x0087ff, 0x00af00, 0x00af5f, 0x00af87, 0x00afaf, 0x00afd7, 0x00afff,
        0x00d700, 0x00d75f, 0x00d787, 0x00d7af, 0x00d7d7, 0x00d7ff, 0x00ff00, 0x00ff5f,
        0x00ff87, 0x00ffaf, 0x00ffd7, 0x00ffff, 0x5f0000, 0x5f005f, 0x5f0087, 0x5f00af,
        0x5f00d7, 0x5f00ff, 0x5f5f00, 0x5f5f5f, 0x5f5f87, 0x5f5faf, 0x5f5fd7, 0x5f5fff,
        0x5f8700, 0x5f875f, 0x5f8787, 0x5f87af, 0x5f87d7, 0x5f87ff, 0x5faf00, 0x5faf5f,
        0x5faf87, 0x5fafaf, 0x5fafd7, 0x5fafff, 0x5fd700, 0x5fd75f, 0x5fd787, 0x5fd7af,
        0x5fd7d7, 0x5fd7ff, 0x5fff00, 0x5fff5f, 0x5fff87, 0x5fffaf, 0x5fffd7, 0x5fffff,
        0x870000, 0x87005f, 0x870087, 0x8700af, 0x8700d7, 0x8700ff, 0x875f00, 0x875f5f,
        0x875f87, 0x875faf, 0x875fd7, 0x875fff, 0x878700, 0x87875f, 0x878787, 0x8787af,
        0x8787d7, 0x8787ff, 0x87af00, 0x87af5f, 0x87af87, 0x87afaf, 0x87afd7, 0x87afff,
        0x87d700, 0x87d75f, 0x87d787, 0x87d7af, 0x87d7d7, 0x87d7ff, 0x87ff00, 0x87ff5f,
        0x87ff87, 0x87ffaf, 0x87ffd7, 0x87ffff, 0xaf0000, 0xaf005f, 0xaf0087, 0xaf00af,
        0xaf00d7, 0xaf00ff, 0xaf5f00, 0xaf5f5f, 0xaf5f87, 0xaf5faf, 0xaf5fd7, 0xaf5fff,
        0xaf8700, 0xaf875f, 0xaf8787, 0xaf87af, 0xaf87d7, 0xaf87ff, 0xafaf00, 0xafaf5f,
        0xafaf87, 0xafafaf, 0xafafd7, 0xafafff, 0xafd700, 0xafd75f, 0xafd787, 0xafd7af,
        0xafd7d7, 0xafd7ff, 0xafff00, 0xafff5f, 0xafff87, 0xafffaf, 0xafffd7, 0xafffff,
        0xd70000, 0xd7005f, 0xd70087, 0xd700af, 0xd700d7, 0xd700ff, 0xd75f00, 0xd75f5f,
        0xd75f87, 0xd75faf, 0xd75fd7, 0xd75fff, 0xd78700, 0xd7875f, 0xd78787, 0xd787af,
        0xd787d7, 0xd787ff, 0xd7af00, 0xd7af5f, 0xd7af87, 0xd7afaf, 0xd7afd7, 0xd7afff,
        0xd7d700, 0xd7d75f, 0xd7d787, 0xd7d7af, 0xd7d7d7, 0xd7d7ff, 0xd7ff00, 0xd7ff5f,
        0xd7ff87, 0xd7ffaf, 0xd7ffd7, 0xd7ffff, 0xff0000, 0xff005f, 0xff0087, 0xff00af,
        0xff00d7, 0xff00ff, 0xff5f00, 0xff5f5f, 0xff5f87, 0xff5faf, 0xff5fd7, 0xff5fff,
        0xff8700, 0xff875f, 0xff8787, 0xff87af, 0xff87d7, 0xff87ff, 0xffaf00, 0xffaf5f,
        0xffaf87, 0xffafaf, 0xffafd7, 0xffafff, 0xffd700, 0xffd75f, 0xffd787, 0xffd7af,
        0xffd7d7, 0xffd7ff, 0xffff00, 0xffff5f, 0xffff87, 0xffffaf, 0xffffd7, 0xffffff,
        0x080808, 0x121212, 0x1c1c1c, 0x262626, 0x303030, 0x3a3a3a, 0x444444, 0x4e4e4e,
        0x585858, 0x626262, 0x6c6c6c, 0x767676, 0x808080, 0x8a8a8a, 0x949494, 0x9e9e9e,
        0xa8a8a8, 0xb2b2b2, 0xbcbcbc, 0xc6c6c6, 0xd0d0d0, 0xdadada, 0xe4e4e4, 0xeeeeee,
    ))
    config_paths: typing.Tuple[str, ...] = ()
    config_overrides: typing.Tuple[str, ...] = ()

    def __init__(self, options_dict: typing.Optional[typing.Dict[str, typing.Any]] = None) -> None:
        self.color_table = array(self.color_table.typecode, self.color_table)
        if options_dict is not None:
            null = object()
            for key in option_names:
                val = options_dict.get(key, null)
                if val is not null:
                    setattr(self, key, val)

    @property
    def _fields(self) -> typing.Tuple[str, ...]:
        return option_names

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._fields)

    def __len__(self) -> int:
        return len(self._fields)

    def _copy_of_val(self, name: str) -> typing.Any:
        ans = getattr(self, name)
        if isinstance(ans, dict):
            ans = ans.copy()
        elif isinstance(ans, list):
            ans = ans[:]
        return ans

    def _asdict(self) -> typing.Dict[str, typing.Any]:
        return {k: self._copy_of_val(k) for k in self}

    def _replace(self, **kw: typing.Any) -> "Options":
        ans = Options()
        for name in self:
            setattr(ans, name, self._copy_of_val(name))
        for name, val in kw.items():
            setattr(ans, name, val)
        return ans

    def __getitem__(self, key: typing.Union[int, str]) -> typing.Any:
        k = option_names[key] if isinstance(key, int) else key
        try:
            return getattr(self, k)
        except AttributeError:
            pass
        raise KeyError(f"No option named: {k}")

    def __getattr__(self, key: str) -> typing.Any:
        if key.startswith("color"):
            q = key[5:]
            if q.isdigit():
                k = int(q)
                if 0 <= k <= 255:
                    x = self.color_table[k]
                    return Color((x >> 16) & 255, (x >> 8) & 255, x & 255)
        raise AttributeError(key)

    def __setattr__(self, key: str, val: typing.Any) -> typing.Any:
        if key.startswith("color"):
            q = key[5:]
            if q.isdigit():
                k = int(q)
                if 0 <= k <= 255:
                    self.color_table[k] = int(val)
                    return
        object.__setattr__(self, key, val)


defaults = Options()
defaults.action_alias = {}
defaults.env = {}
defaults.exe_search_path = {}
defaults.font_features = {}
defaults.kitten_alias = {}
defaults.symbol_map = {}
defaults.watcher = {}
defaults.map = [
    # copy_to_clipboard
    KeyDefinition(trigger=SingleKey(mods=1024, key=99), definition='copy_to_clipboard'),  # noqa
    # paste_from_clipboard
    KeyDefinition(trigger=SingleKey(mods=1024, key=118), definition='paste_from_clipboard'),  # noqa
    # paste_from_selection
    KeyDefinition(trigger=SingleKey(mods=1024, key=115), definition='paste_from_selection'),  # noqa
    # paste_from_selection
    KeyDefinition(trigger=SingleKey(mods=1, key=57348), definition='paste_from_selection'),  # noqa
    # pass_selection_to_program
    KeyDefinition(trigger=SingleKey(mods=1024, key=111), definition='pass_selection_to_program'),  # noqa
    # scroll_line_up
    KeyDefinition(trigger=SingleKey(mods=1024, key=57352), definition='scroll_line_up'),  # noqa
    # scroll_line_up
    KeyDefinition(trigger=SingleKey(mods=1024, key=107), definition='scroll_line_up'),  # noqa
    # scroll_line_down
    KeyDefinition(trigger=SingleKey(mods=1024, key=57353), definition='scroll_line_down'),  # noqa
    # scroll_line_down
    KeyDefinition(trigger=SingleKey(mods=1024, key=106), definition='scroll_line_down'),  # noqa
    # scroll_page_up
    KeyDefinition(trigger=SingleKey(mods=1024, key=57354), definition='scroll_page_up'),  # noqa
    # scroll_page_down
    KeyDefinition(trigger=SingleKey(mods=1024, key=57355), definition='scroll_page_down'),  # noqa
    # scroll_home
    KeyDefinition(trigger=SingleKey(mods=1024, key=57356), definition='scroll_home'),  # noqa
    # scroll_end
    KeyDefinition(trigger=SingleKey(mods=1024, key=57357), definition='scroll_end'),  # noqa
    # scroll_to_previous_prompt
    KeyDefinition(trigger=SingleKey(mods=1024, key=122), definition='scroll_to_prompt -1'),  # noqa
    # scroll_to_next_prompt
    KeyDefinition(trigger=SingleKey(mods=1024, key=120), definition='scroll_to_prompt 1'),  # noqa
    # show_scrollback
    KeyDefinition(trigger=SingleKey(mods=1024, key=104), definition='show_scrollback'),  # noqa
    # show_last_command_output
    KeyDefinition(trigger=SingleKey(mods=1024, key=103), definition='show_last_command_output'),  # noqa
    # new_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=57345), definition='new_window'),  # noqa
    # new_os_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=110), definition='new_os_window'),  # noqa
    # close_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=119), definition='close_window'),  # noqa
    # next_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=93), definition='next_window'),  # noqa
    # previous_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=91), definition='previous_window'),  # noqa
    # move_window_forward
    KeyDefinition(trigger=SingleKey(mods=1024, key=102), definition='move_window_forward'),  # noqa
    # move_window_backward
    KeyDefinition(trigger=SingleKey(mods=1024, key=98), definition='move_window_backward'),  # noqa
    # move_window_to_top
    KeyDefinition(trigger=SingleKey(mods=1024, key=96), definition='move_window_to_top'),  # noqa
    # start_resizing_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=114), definition='start_resizing_window'),  # noqa
    # first_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=49), definition='first_window'),  # noqa
    # second_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=50), definition='second_window'),  # noqa
    # third_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=51), definition='third_window'),  # noqa
    # fourth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=52), definition='fourth_window'),  # noqa
    # fifth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=53), definition='fifth_window'),  # noqa
    # sixth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=54), definition='sixth_window'),  # noqa
    # seventh_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=55), definition='seventh_window'),  # noqa
    # eighth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=56), definition='eighth_window'),  # noqa
    # ninth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=57), definition='ninth_window'),  # noqa
    # tenth_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=48), definition='tenth_window'),  # noqa
    # focus_visible_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=57370), definition='focus_visible_window'),  # noqa
    # swap_with_window
    KeyDefinition(trigger=SingleKey(mods=1024, key=57371), definition='swap_with_window'),  # noqa
    # next_tab
    KeyDefinition(trigger=SingleKey(mods=1024, key=57351), definition='next_tab'),  # noqa
    # next_tab
    KeyDefinition(trigger=SingleKey(mods=4, key=57346), definition='next_tab'),  # noqa
    # previous_tab
    KeyDefinition(trigger=SingleKey(mods=1024, key=57350), definition='previous_tab'),  # noqa
    # previous_tab
    KeyDefinition(trigger=SingleKey(mods=5, key=57346), definition='previous_tab'),  # noqa
    # new_tab
    KeyDefinition(trigger=SingleKey(mods=1024, key=116), definition='new_tab'),  # noqa
    # close_tab
    KeyDefinition(trigger=SingleKey(mods=1024, key=113), definition='close_tab'),  # noqa
    # move_tab_forward
    KeyDefinition(trigger=SingleKey(mods=1024, key=46), definition='move_tab_forward'),  # noqa
    # move_tab_backward
    KeyDefinition(trigger=SingleKey(mods=1024, key=44), definition='move_tab_backward'),  # noqa
    # set_tab_title
    KeyDefinition(trigger=SingleKey(mods=1026, key=116), definition='set_tab_title'),  # noqa
    # next_layout
    KeyDefinition(trigger=SingleKey(mods=1024, key=108), definition='next_layout'),  # noqa
    # increase_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=61), definition='change_font_size all +2.0'),  # noqa
    # increase_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=43), definition='change_font_size all +2.0'),  # noqa
    # increase_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=57413), definition='change_font_size all +2.0'),  # noqa
    # decrease_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=45), definition='change_font_size all -2.0'),  # noqa
    # decrease_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=57412), definition='change_font_size all -2.0'),  # noqa
    # reset_font_size
    KeyDefinition(trigger=SingleKey(mods=1024, key=57347), definition='change_font_size all 0'),  # noqa
    # open_url
    KeyDefinition(trigger=SingleKey(mods=1024, key=101), definition='open_url_with_hints'),  # noqa
    # insert_selected_path
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=102),), definition='kitten hints --type path --program -'),  # noqa
    # open_selected_path
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(mods=1, key=102),), definition='kitten hints --type path'),  # noqa
    # insert_selected_line
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=108),), definition='kitten hints --type line --program -'),  # noqa
    # insert_selected_word
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=119),), definition='kitten hints --type word --program -'),  # noqa
    # insert_selected_hash
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=104),), definition='kitten hints --type hash --program -'),  # noqa
    # goto_file_line
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=110),), definition='kitten hints --type linenum'),  # noqa
    # open_selected_hyperlink
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=112), rest=(SingleKey(key=121),), definition='kitten hints --type hyperlink'),  # noqa
    # toggle_fullscreen
    KeyDefinition(trigger=SingleKey(mods=1024, key=57374), definition='toggle_fullscreen'),  # noqa
    # toggle_maximized
    KeyDefinition(trigger=SingleKey(mods=1024, key=57373), definition='toggle_maximized'),  # noqa
    # input_unicode_character
    KeyDefinition(trigger=SingleKey(mods=1024, key=117), definition='kitten unicode_input'),  # noqa
    # edit_config_file
    KeyDefinition(trigger=SingleKey(mods=1024, key=57365), definition='edit_config_file'),  # noqa
    # kitty_shell
    KeyDefinition(trigger=SingleKey(mods=1024, key=57344), definition='kitty_shell window'),  # noqa
    # increase_background_opacity
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=97), rest=(SingleKey(key=109),), definition='set_background_opacity +0.1'),  # noqa
    # decrease_background_opacity
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=97), rest=(SingleKey(key=108),), definition='set_background_opacity -0.1'),  # noqa
    # full_background_opacity
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=97), rest=(SingleKey(key=49),), definition='set_background_opacity 1'),  # noqa
    # reset_background_opacity
    KeyDefinition(is_sequence=True, trigger=SingleKey(mods=1024, key=97), rest=(SingleKey(key=100),), definition='set_background_opacity default'),  # noqa
    # reset_terminal
    KeyDefinition(trigger=SingleKey(mods=1024, key=57349), definition='clear_terminal reset active'),  # noqa
    # reload_config_file
    KeyDefinition(trigger=SingleKey(mods=1024, key=57368), definition='load_config_file'),  # noqa
    # debug_config
    KeyDefinition(trigger=SingleKey(mods=1024, key=57369), definition='debug_config'),  # noqa
]
if is_macos:
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=99), definition='copy_to_clipboard'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=118), definition='paste_from_clipboard'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=10, key=57354), definition='scroll_line_up'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57352), definition='scroll_line_up'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=10, key=57355), definition='scroll_line_down'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57353), definition='scroll_line_down'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57354), definition='scroll_page_up'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57355), definition='scroll_page_down'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57356), definition='scroll_home'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57357), definition='scroll_end'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57345), definition='new_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=110), definition='new_os_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=100), definition='close_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=114), definition='start_resizing_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=49), definition='first_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=50), definition='second_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=51), definition='third_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=52), definition='fourth_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=53), definition='fifth_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=54), definition='sixth_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=55), definition='seventh_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=56), definition='eighth_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=57), definition='ninth_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=93), definition='next_tab'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=91), definition='previous_tab'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=116), definition='new_tab'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=119), definition='close_tab'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=119), definition='close_os_window'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=105), definition='set_tab_title'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=43), definition='change_font_size all +2.0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=61), definition='change_font_size all +2.0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=61), definition='change_font_size all +2.0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=45), definition='change_font_size all -2.0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=9, key=45), definition='change_font_size all -2.0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=48), definition='change_font_size all 0'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=10, key=115), definition='toggle_macos_secure_keyboard_entry'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=12, key=32), definition='kitten unicode_input'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=8, key=44), definition='edit_config_file'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=10, key=114), definition='clear_terminal reset active'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=12, key=44), definition='load_config_file'))  # noqa
    defaults.map.append(KeyDefinition(trigger=SingleKey(mods=10, key=44), definition='debug_config'))  # noqa
defaults.mouse_map = [
    # click_url_or_select
    MouseMapping(repeat_count=-2, definition='mouse_handle_click selection link prompt'),  # noqa
    # click_url_or_select_grabbed
    MouseMapping(mods=1, repeat_count=-2, grabbed=True, definition='mouse_handle_click selection link prompt'),  # noqa
    # click_url_or_select_grabbed
    MouseMapping(mods=1, repeat_count=-2, definition='mouse_handle_click selection link prompt'),  # noqa
    # click_url
    MouseMapping(mods=5, repeat_count=-1, grabbed=True, definition='mouse_handle_click link'),  # noqa
    # click_url
    MouseMapping(mods=5, repeat_count=-1, definition='mouse_handle_click link'),  # noqa
    # click_url_discard
    MouseMapping(mods=5, grabbed=True, definition='discard_event'),  # noqa
    # paste_selection
    MouseMapping(button=2, repeat_count=-1, definition='paste_from_selection'),  # noqa
    # start_simple_selection
    MouseMapping(definition='mouse_selection normal'),  # noqa
    # start_rectangle_selection
    MouseMapping(mods=6, definition='mouse_selection rectangle'),  # noqa
    # select_word
    MouseMapping(repeat_count=2, definition='mouse_selection word'),  # noqa
    # select_line
    MouseMapping(repeat_count=3, definition='mouse_selection line'),  # noqa
    # select_line_from_point
    MouseMapping(mods=6, repeat_count=3, definition='mouse_selection line_from_point'),  # noqa
    # extend_selection
    MouseMapping(button=1, definition='mouse_selection extend'),  # noqa
    # paste_selection_grabbed
    MouseMapping(button=2, mods=1, repeat_count=-1, grabbed=True, definition='paste_selection'),  # noqa
    # paste_selection_grabbed
    MouseMapping(button=2, mods=1, repeat_count=-1, definition='paste_selection'),  # noqa
    # paste_selection_grabbed
    MouseMapping(button=2, mods=1, grabbed=True, definition='discard_event'),  # noqa
    # start_simple_selection_grabbed
    MouseMapping(mods=1, grabbed=True, definition='mouse_selection normal'),  # noqa
    # start_simple_selection_grabbed
    MouseMapping(mods=1, definition='mouse_selection normal'),  # noqa
    # start_rectangle_selection_grabbed
    MouseMapping(mods=7, grabbed=True, definition='mouse_selection rectangle'),  # noqa
    # start_rectangle_selection_grabbed
    MouseMapping(mods=7, definition='mouse_selection rectangle'),  # noqa
    # select_word_grabbed
    MouseMapping(mods=1, repeat_count=2, grabbed=True, definition='mouse_selection word'),  # noqa
    # select_word_grabbed
    MouseMapping(mods=1, repeat_count=2, definition='mouse_selection word'),  # noqa
    # select_line_grabbed
    MouseMapping(mods=1, repeat_count=3, grabbed=True, definition='mouse_selection line'),  # noqa
    # select_line_grabbed
    MouseMapping(mods=1, repeat_count=3, definition='mouse_selection line'),  # noqa
    # select_line_from_point_grabbed
    MouseMapping(mods=7, repeat_count=3, grabbed=True, definition='mouse_selection line_from_point'),  # noqa
    # select_line_from_point_grabbed
    MouseMapping(mods=7, repeat_count=3, definition='mouse_selection line_from_point'),  # noqa
    # extend_selection_grabbed
    MouseMapping(button=1, mods=1, grabbed=True, definition='mouse_selection extend'),  # noqa
    # extend_selection_grabbed
    MouseMapping(button=1, mods=1, definition='mouse_selection extend'),  # noqa
    # show_clicked_cmd_output_ungrabbed
    MouseMapping(button=1, mods=5, definition='mouse_show_command_output'),  # noqa
]
