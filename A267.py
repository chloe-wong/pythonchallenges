def BinarySearch(List,SearchItem):
   Low = min(List)
   High = max(List)
   Index = -1    
   while (Index == -1) and (Low <= High):
      Middle = (High + Low) // 2       
      if List[Middle] == SearchItem:          
         Index = Middle       
      elif List[Middle] < SearchItem:          
          Low = Middle + 1       
      else:
         High = Middle - 1
   return(Index)

List = [3,1,9,8,4,5]
SearchItem = 3
firstresult = BinarySearch(List, SearchItem)
if firstresult == -1:
   print("initial binary search returns: False. Performing second binary search on the sorted list...")
   List.sort()
   secondresult = BinarySearch(List, SearchItem)
   if secondresult == -1:
      print("the item is not in the list")
   else:
      print("the item is at index:", secondresult, "in the sorted list")
else:
   print("item is at index:",firstresult)
