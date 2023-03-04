"""
Неофициальная редакция для CSoft Model Studio COM API
https://github.com/GeorgGrebenyuk/cs_modelstudio_com_api_about
Демонстрационный пример работы с MS COM API (UnitsCSCom) -- Model Studio Objects 1.0 Type Library из Python
На примере проекта MS_Трубопроводы_Проект.dwg (может быть любой ваш проект)
"""
import win32com.client
#Проверка, является принадлежит ли объект ModelStudio, как запрос у элемента поля-интерфейса Element (CElement)
def is_object_of_ms(checking_object):
    try:
        check_element = checking_object.Element
        if check_element is not None:
            return True
        else:
            return False
    except:
        return False

#Подсчет числа объектов каждого класса (для наглядного сравнения с моделью)
def calc_objects_classes(block_space):
    class2objects_count = dict()
    for object_in_block in block_space:
        o_name = object_in_block.EntityName
        if o_name not in class2objects_count.keys():
            class2objects_count[o_name] = 1
        else:
            class2objects_count[o_name] += 1
    return class2objects_count

#In general "nanocad.Application"
nanocad_app = win32com.client.Dispatch("nanoCADx64.Application.22.0")
if nanocad_app is not None:
    ncad_doc = nanocad_app.ActiveDocument
    if ncad_doc is not None:
        print("Doc is exist" + ncad_doc.Name)
        model_space = ncad_doc.ModelSpace
        """
        Выводим число объектов модели одного класса, удобно сравнивать с пользовательским выделением объектов в модели
        """
        print(str(calc_objects_classes(model_space)))

        #Обычный перебор объектов модели MS и обработка объектов MS Трубопроводы
        for object_in_block in model_space:

            #Позиционирование объекта как трассы трубопровода, интерфейс IWrAxis
            def IWrAxis_work():
                o_as_IWrAxis = win32com.client.CastTo(object_in_block, "IWrAxis")
                print("CountItems = " + str(o_as_IWrAxis.CountItems(True, True, True, True, True)))
                print("HasEquipmentNodeStart = " + str(o_as_IWrAxis.HasEquipmentNodeStart))
                print("HasEquipmentNodeEnd  = " + str(o_as_IWrAxis.HasEquipmentNodeEnd))
                pass
            #Позиционирование объекта как произвольного элемента на оси трубопровода (общий класс для всех типов элементов)
            def IWrNodeElbow_work():
                o_as_WrNodeElbow = win32com.client.CastTo(object_in_block, "IWrNodeElbow")
                print("OrderOnLine = " + str(o_as_WrNodeElbow.OrderOnLine))
                pass
            def IWrSegment_work():
                o_as_WrSegment = win32com.client.CastTo(object_in_block, "IWrSegment")
                el_ElementSubSeg = o_as_WrSegment.ElementSubSeg
                print("ElementSubSeg = " + el_ElementSubSeg.Name)
                pass
            def IWrSupport_work():
                o_as_WrSuppor = win32com.client.CastTo(object_in_block, "IWrSupport")
                print(o_as_WrSuppor.PipeLayer)
                pass
            if is_object_of_ms(object_in_block):
                ms_object = object_in_block.Element
                print("\n name of MS Object = " + ms_object.Name + " , Descr. = " + ms_object.Description)

                if ms_object.Name == "Труба":
                    print("Приведение к интерфейсу IWrSegment")
                    IWrSegment_work()
                if object_in_block.EntityName == "vCSAxis":
                    print("Приведение к интерфейсу IWrAxis")
                    IWrAxis_work()
                if object_in_block.EntityName == "vCSNode":
                    print("Приведение к интерфейсу IWrNodeElbow")
                    IWrNodeElbow_work()

    else:
        print("Doc not running")
else:
    print("App not running")