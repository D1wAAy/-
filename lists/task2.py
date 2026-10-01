requests = ["ПК-1", "ПК-2", "ПК-3"]
requests.append("ПК-4")
requests.insert(0, "Срочно")
requests[2] = "ПК-2 исправлен"
requests.remove("ПК-3")
last_requests=requests.pop()
print(last_requests)
print(requests)