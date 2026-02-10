import { Component, OnInit } from '@angular/core';
import { WordsmithService } from "../wordsmith.service";
import { WordTypeArray } from "../wordsmith";
import { MatRadioChange } from "@angular/material/radio";


@Component({
  selector: 'app-wordsmith',
  templateUrl: './wordsmith.component.html',
  styleUrls: ['./wordsmith.component.css']
})
export class WordsmithComponent implements OnInit {

  wordsmithData: WordTypeArray = [];
  // question: Question|null = null;
  // answer: Answer|null = null;
  disableRadioButtons: boolean = false;
  disableNextButton: boolean = true;
  questionNumber: number = 0;
  correctAnswers: number = 0;

  constructor(private wordsmithService: WordsmithService) { }

  ngOnInit(): void {
    this.getWordTypes();
  }

  getWordTypes() {
    this.wordsmithService.getWordTypes().subscribe({
        next: (data) => {
          console.log(data);
          this.wordsmithData = data;
          //this.getNextQuestion();
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

  // getNextQuestion() {
  //   if (this.wordsmithData.length) {
  //     const index = Math.floor(Math.random() * this.wordsmithData.length);
  //     this.question = this.wordsmithData[index];
  //     this.wordsmithData.splice(index, 1);
  //   } else {
  //     this.question = null;
  //   }
  //
  //   if (this.answer) {
  //     this.questionNumber++;
  //     if (this.answer.is_correct) {
  //       this.correctAnswers++;
  //     }
  //   }
  //
  //   this.answer = null;
  //   this.disableRadioButtons = false;
  //   this.disableNextButton = true;
  // }

  // getCorrectAnswer() {
  //   if (this.question) {
  //     return this.question.answers.filter(answer => answer.is_correct)[0].answer;
  //   }
  //   return '';
  // }
  //
  // answerSelected(event: MatRadioChange) {
  //   this.disableRadioButtons = true;
  //   this.disableNextButton = false;
  // }

}
