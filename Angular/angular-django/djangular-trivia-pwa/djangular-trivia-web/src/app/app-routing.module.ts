import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TriviaComponent } from "./trivia/trivia.component";
import { WordsmithComponent } from "./wordsmith/wordsmith.component";

const routes: Routes = [
  { path: '', component: TriviaComponent },
  { path: 'words', component: WordsmithComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
