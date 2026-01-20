# Internationalization and Localization - Community Edition

A collection of localizations all in one place, for the convenience of the hell diver.

# Contributing

In order to contribute, your Pull Request must ensure the following structure

```powershell
locales/
└── en-US/
    ├── _manifest.json
    ├── flag.png          # 64x64px recommended
    └── translations/
        ├── dialogs.json
        ├── menus.json
        ╎ 
```

In order to find out what you should name the folder for your language, please refer to the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) which defines the **xx-XX** model (language-COUNTRY), along with the list of language codes from [ISO 639-2](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) [[Backup](https://www.loc.gov/standards/iso639-2/php/code_list.php)] and the list of country codes as defined by the [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes) [[Backup](https://www.iso.org/obp/ui/#search)] standard. 

For example, if you wanted to write the translation for **Brazilian Portuguese**, you'd write it as **`pt-BR`**

For the flag, you may use Twemoji, asa it is the simplest shape and most commonly used online. You can get them here 
[[1] Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/) 
[[2] Emojipedia](https://emojipedia.org/twitter)