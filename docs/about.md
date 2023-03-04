# О файлах

Настоящая папка содержит сгенерированную в формате CHM справку к COM API, сформированную по IDL файлам из каталога `\MS_CadLib_API\API\IDL`. 

В сыром виде, IDL файлы описывают разные COM библиотеки с той поправкой, что в конечной системе COM-server представлен не классической библиотекой типов tlb, а скомпилированными библиотеками (в том числе nrx), потому их однозначная идентификация может быть затруднена. В таблице ниже приводится сопоставление некоторых IDL-COM библиотек с их названиями в системе и предназначением.

Указанные в графе __Interop DLL__ названия (и сборки в разделе Releases) были получены путем подключения к проекту в Visual Studio COM библиотек - файлы в директории *bin/Configuration/obj*

IDL Name | Название библиотеки | Идентификатор библиотеки (guid) |Файл COM-server | Interop DLL | C++ API | Предназначение
--| -- | -- | --| -- | -- | --
SchematiCSCOM.idl | Model Studio CS Schema 1.0 Type Library | 0186D491-6D1A-496d-8E1C-94427E1F66D2 | SchematiCSCOM.nrx | Interop.SchematiCSCOMLib.dll | `\Stable_API\Model Studio CS\Source\SchematiCSCOM` | (?) Доступ к объектной модели ModelStudio Технологические Системы
ViperCSObjCom.idl | vCSViperCSObjCom 1.0 Type Library| F4A0D05F-A659-4EEC-9021-DCF12867B9B8| ViperCSObjCom.nrx | Interop.vCSViperCSObjComLib.dll |`\Stable_API\Model Studio CS\Source\ViperCSObjCom` | Описание интерфейсов объектов трубопроводов (для MS Трубопроводы)
UnitsCSCom.idl | Model Studio Objects 1.0 Type Library | 1AE1985C-5D87-4E89-8E67-068628FC3CD6 | UnitsCSCom.nrx | Interop.mdsUnitsLib.dll | `\Stable_API\Model Studio CS\Source\UnitsCSCom` | Описание интерфейсов стандартного оборудования и доступ к параметрам объектов MS
URS.idl |Model Studio Unified Reporting Service 1.0 Type Library | 70A33123-81A3-4C4B-8A90-CFEDD3A35994 | URS.nrx | Interop.mdsURSLib.dll | `\Stable_API\Model Studio CS\Source\URS` | Описание профиля (настроек) для отчетов у системы документирования ModelStudio. [1]
LibManager.idl | Model Studio Library Manager 1.0 Type Library | 1EB7B184-2C93-4DB2-97E8-2F8A392495C1 | lcsLibManager.nrx | Interop.mdsLibManagerLib.dll | `\Stable_API\Model Studio CS\Source\LibManager`| (?) Работа с библиотекой стандартных компонентов
linCSCom.idl | Model Studio ELAY Objects 1.0 Type Library | DF15E75B-C049-49EE-881F-DAA87873E483 | linCSCom.nrx | Interop.mdsELAYComLib.dll | `\Stable_API\Model Studio CS\Source\linCSCom` | Интерфейсы для MS ELAY (ОРУ: Открытые распределительные устройства)
ironObjCom.idl | ironObjCom 1.0 Type Library | 1EBC5053-9B5A-4D3B-A5D4-F0B3C61CB4D1 | ironObjCom.nrx | Interop.ironObjComLib.dll | `\Stable_API\Model Studio CS\Source\ironObjCom` | ??? [2]
LotsiaCadLibPlugin.idl | Нет данных | (?) 56B78070-FB21-489D-94FE-685BFD9397C4 | Нет данных| Нет данных | `\Stable_API\Model Studio CS\Source\msMPHS\LotsiaCadLibPlugin\LotsiaCadLibPlugin` | (?) Шаблон для создания проектов под Cadlib судя по readme
msCABCom.idl | msCABCom 1.0 Type Library | 81D3F477-6153-4C9E-9497-FE20C1D4C7FC | msCABCom.nrx | Interop.msCABComLib.dll | `\Stable_API\Model Studio CS\Source\msCABCom` | Нет данных
msMPHS.idl | mstmsMPHS 1.0 Type Library | EF016163-4CF6-4868-9236-CCCA8BC0318D | msMPHS.nrx | Нет данных |  `\Stable_API\Model Studio CS\Source\msMPHS` | Нет данных
MSStormCom.idl | Model Studio STORM Objects 1.0 Type Library | 21AB607E-30A2-4779-9C1B-6EEDC77A8E0E | csMSStormCom.nrx | Interop.CSMSStormComLib.dll |`\Stable_API\Model Studio CS\Source\MSStormCom` | Интерфейсы для MS Storm (Молниезащита)
mstHVACCOM.idl | mstHVACCOM 1.0 Type Library | B491E8A1-16A1-4FDC-A4F5-15313C541987 |mstHVACCOM.nrx | Interop.mstHVACCOMLib.dll | `\Stable_API\Model Studio CS\Source\mstHVACCom` | Нет данных [3]
mstMetalCOM.idl | Model Studio Cable 1.0 Type Library | DABD1F91-8747-4606-BDBE-EE5EE247CC38 | mstMetalCOM.nrx | Interop.mdsMetalLib.dll | `\Stable_API\Model Studio CS\Source\mstMetalCOM`| Интерфейсы для MS Cable (Кабельное хозяйство)
mstProjectCOM.idl | mstProjectCOM 1.0 Type Library | 0F11628B-DFE5-45FF-B0BE-F610AFC63EE6 | mstProjectCOM.nrx | Interop.mstProjectCOMLib.dll | `\Stable_API\Model Studio CS\Source\mstProjectCom` | Нет данных [4]
mstRouteCOM.idl | mstRouteCOM 1.0 Type Library | B491E8A1-16A1-4FDC-A4F5-15313C547E72 | mstRouteCom.nrx | Interop.mstRouteCOMLib.dll | `\Stable_API\Model Studio CS\Source\mstRouteCom` |  Нет данных [5]
NWEViewerComponent.idl | Interop.NWEViewerComponentLib | Нет данных| Interop.NWEViewerComponentLib.dll | `\Stable_API\Model Studio CS\Source\ViewerComponent\NWEViewerComponent` | (?) Компонент для работы со сценой модели и камерой
p4darx2dlayout.idl | p4darx-2dlayout 1.0 Type Library | E2A750C7-1A29-4B75-9E5B-B26230AD5A1B | Нет данных | Нет данных | Нет данных | Нет данных
ProfileView.idl | Model Studio LINE 1.0 Type Library | 4CE7FBFF-1896-44CB-B18A-A59F8BEA4584 | Нет данных  | Нет данных | `\Stable_API\Model Studio CS\Source\ProfileView` | Нет данных [6]
ProfileViewCOM.idl | Model Studio LINE Objects 1.0 Type Library | CEC0A97B-2CAF-4592-8F9E-05AA1A046A04 | ProfileViewCOM.nrx, ProfileViewObjects.nrx | Interop.mdsLINEComLib.dll | `\Stable_API\Model Studio CS\Source\ProfileViewCOM`, `\Stable_API\Model Studio CS\Source\ProfileViewObjects` | нет данных [6]
SCXComponentsLib.idl | SCXComponentsLib 1.0 Type Library | F892997C-0DAF-41C0-8698-08A1051A491B | Нет данных | Interop.SCXComponentsLibLib.dll | `\Stable_API\Model Studio CS\Source\SCXComponentsLib` | Нет данных 
ShieldCSCOM.idl | CSShieldCSCOM 1.0 Type Library | 8A409328-0318-49DD-98A0-5E90E5668A65 | Нет данных | Нет данных | `\Stable_API\Model Studio CS\Source\ShieldCSCom` | (?) Возможно, Компоновщик щитов
rvm.idl | Нет данных | Нет данных | (?) rvmManager.dll |  Нет данных | `\Stable_API\Model Studio CS\Source\rvm`, `\Stable_API\Model Studio CS\Source\rvmManager` |  Нет данных 



## Примечания:

[1]: Интерфейс называется IURSApplication, метод для получения отчета – CreateReport. В качестве параметра туда можно передать название профиля экспорта из настроек MS, полный путь к профилю экспорта или профиль экспорта в виде MSXMLDom. На выходе получается COM-объект типа MSXMLDom.

[2]: Судя по внутренним интерфейсам, что-то общее для AEC компонентов

[3]: Созвучно с HVAC Solutions (https://hvacsolutions.com)

[4]: Возможно, для подсистемы документирования

[5]: Возможно что-то для трасс прокладки коммуникаций

[6]: Возможно, база для ProfileViewObjects, ProfileViewCOM. Возможно для MS PLine (ЛЭП)
