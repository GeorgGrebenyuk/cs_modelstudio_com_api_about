# О файлах

Настоящая папка содержит сгенерированную в формате CHM справку к COM API, сформированную по IDL файлам из каталога `\MS_CadLib_API\API\IDL`. 

В сыром виде, IDL файлы описывают разные COM библиотеки с той поправкой, что в конечной системе COM-server представлен не классической библиотекой типов tlb, а скомпилированными библиотеками (в том числе nrx), потому их однозначная идентификация может быть затруднена. В таблице ниже приводится сопоставление некоторых IDL-COM библиотек с их названиями в системе и предназначением

IDL Name | Название библиотеки | Идентификатор библиотеки (guid) |Файл COM-server | Interop DLL | C++ API | Комментарий
--| -- | -- | --| -- | -- | --
SchematiCSCOM.idl | Model Studio CS Schema 1.0 Type Library | 0186D491-6D1A-496d-8E1C-94427E1F66D2 | SchematiCSCOM.nrx | Interop.SchematiCSCOMLib.dll | `\Stable_API\Model Studio CS\Source\SchematiCSCOM` | (?) Доступ к объектной модели ModelStudio
ViperCSObjCom.idl | vCSViperCSObjCom 1.0 Type Library| F4A0D05F-A659-4EEC-9021-DCF12867B9B8| ViperCSObjCom.nrx | Interop.vCSViperCSObjComLib.dll |`\Stable_API\Model Studio CS\Source\ViperCSObjCom` | Описание интерфейсов объектов трубопроводов
UnitsCSCom.idl | Model Studio Objects 1.0 Type Library | 1AE1985C-5D87-4E89-8E67-068628FC3CD6 | UnitsCSCom.nrx | Отсутствует | `\Stable_API\Model Studio CS\Source\UnitsCSCom` | Описание интерфейсов стандартного оборудования и доступ к параметрам объектов MS
URS.idl |Model Studio Unified Reporting Service 1.0 Type Library | 70A33123-81A3-4C4B-8A90-CFEDD3A35994 | URS.nrx | Interop.mdsURSLib.dll | `\Stable_API\Model Studio CS\Source\URS` | Описание профиля (настроек) для отчетов у системы документирования ModelStudio. Интерфейс называется IURSApplication, метод для получения отчета – CreateReport. В качестве параметра туда можно передать название профиля экспорта из настроек MS, полный путь к профилю экспорта или профиль экспорта в виде MSXMLDom. На выходе получается COM-объект типа MSXMLDom.
