# О файлах

Настоящая папка содержит сгенерированную в формате CHM справку к COM API, сформированную по IDL файлам из каталога `\MS_CadLib_API\API\IDL`. 

В сыром виде, IDL файлы описывают разные COM библиотеки с той поправкой, что в конечной системе COM-server представлен не классической библиотекой типов tlb, а скомпилированными библиотеками (в том числе nrx), потому их однозначная идентификация может быть затруднена. В таблице ниже приводится сопоставление некоторых IDL-COM библиотек с их названиями в системе и предназначением

IDL Name | Название библиотеки | Идентификатор библиотеки (guid) |Файл COM-server | Interop DLL | C++ API | Предназначение
--| -- | -- | --| -- | -- | --
SchematiCSCOM.idl | Model Studio CS Schema 1.0 Type Library | 0186D491-6D1A-496d-8E1C-94427E1F66D2 | SchematiCSCOM.nrx | Interop.SchematiCSCOMLib.dll | `\Stable_API\Model Studio CS\Source\SchematiCSCOM` | (?) Доступ к объектной модели ModelStudio
ViperCSObjCom.idl | vCSViperCSObjCom 1.0 Type Library| F4A0D05F-A659-4EEC-9021-DCF12867B9B8| ViperCSObjCom.nrx | Interop.vCSViperCSObjComLib.dll |`\Stable_API\Model Studio CS\Source\ViperCSObjCom` | Описание интерфейсов объектов трубопроводов (для MS Трубопроводы)
UnitsCSCom.idl | Model Studio Objects 1.0 Type Library | 1AE1985C-5D87-4E89-8E67-068628FC3CD6 | UnitsCSCom.nrx | Interop.mdsUnitsLib.dll | `\Stable_API\Model Studio CS\Source\UnitsCSCom` | Описание интерфейсов стандартного оборудования и доступ к параметрам объектов MS
URS.idl |Model Studio Unified Reporting Service 1.0 Type Library | 70A33123-81A3-4C4B-8A90-CFEDD3A35994 | URS.nrx | Interop.mdsURSLib.dll | `\Stable_API\Model Studio CS\Source\URS` | Описание профиля (настроек) для отчетов у системы документирования ModelStudio. [1]
LibManager.idl | Model Studio Library Manager 1.0 Type Library | 1EB7B184-2C93-4DB2-97E8-2F8A392495C1 | lcsLibManager.nrx | Interop.mdsLibManagerLib.dll | `\Stable_API\Model Studio CS\Source\LibManager`| (?) Работа с библиотекой стандартных компонентов
linCSCom.idl | Model Studio ELAY Objects 1.0 Type Library | DF15E75B-C049-49EE-881F-DAA87873E483 | linCSCom.nrx | Interop.mdsELAYComLib.dll | `\Stable_API\Model Studio CS\Source\linCSCom` | Интерфейсы для MS ELAY (ОРУ: Открытые распределительные устройства)
ironObjCom.idl | ironObjCom 1.0 Type Library | 1EBC5053-9B5A-4D3B-A5D4-F0B3C61CB4D1 | ironObjCom.nrx | Interop.ironObjComLib.dll | `\Stable_API\Model Studio CS\Source\ironObjCom` | ??? [2]
LotsiaCadLibPlugin.idl | Нет данных | (?) 56B78070-FB21-489D-94FE-685BFD9397C4 | Нет данных| Нет данных | `\Stable_API\Model Studio CS\Source\msMPHS\LotsiaCadLibPlugin\LotsiaCadLibPlugin` | (?) Шаблон для создания проектов под Cadlib судя по readme
msCABCom.idl | msCABCom 1.0 Type Library | 81D3F477-6153-4C9E-9497-FE20C1D4C7FC | msCABCom.nrx | Interop.msCABComLib.dll | `\Stable_API\Model Studio CS\Source\msCABCom` | Нет данных
msMPHS.idl | mstmsMPHS 1.0 Type Library | EF016163-4CF6-4868-9236-CCCA8BC0318D | msMPHS.nrx | Нет данных |  `\Stable_API\Model Studio CS\Source\msMPHS` | Нет данных



## Примечания:

[1]: Интерфейс называется IURSApplication, метод для получения отчета – CreateReport. В качестве параметра туда можно передать название профиля экспорта из настроек MS, полный путь к профилю экспорта или профиль экспорта в виде MSXMLDom. На выходе получается COM-объект типа MSXMLDom.
[2]: Судя по внутренним интерфейсам, что-то общее для AEC компонентов
