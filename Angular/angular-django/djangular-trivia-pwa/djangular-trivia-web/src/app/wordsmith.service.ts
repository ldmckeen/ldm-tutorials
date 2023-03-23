import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

import { WordTypeArray } from "./wordsmith";


@Injectable({
 providedIn: 'root'
})
export class WordsmithService {

 constructor(private http: HttpClient) { }

 getWordTypes(): Observable<WordTypeArray> {
   return this.http.get('http://127.0.0.1:9000/word_types/') as Observable<WordTypeArray>;
 }
}
