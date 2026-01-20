# Internationalization and Localization - Community Edition

A collection of localizations all in one place, for the convenience of the hell diver.

# Contributing

In order to contribute, your Pull Request must ensure the following structure

(Similar to [Official Documentation](https://docs.rsnl.gg/localization/creating-packs))

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

For example, if you wanted to write the translation for **Brazilian Portuguese**, you'd write it as 
```
pt-BR
│  └── Country Code
└── Language Code
```

For the flag, you should use [https://flagcdn.com/](https://flagcdn.com/) just as the Arsenal documentation suggests. 

# Helper scripts

The python scripts are meant to help with keeping the repo clean and consistent. You shouldn't have to worry about using them, especially in a PR that wants to add a new language. I will primarily run these periodically myself.