import asyncio
from prisma import Prisma
from response import Response
from user import User
from util import glog

async def create_one_response_core(db: Prisma, response: Response, aimTo: Mood) -> Response:
	aim_to_mood_timestamp = None
	if aimTo != None:
		aim_to_mood_timestamp = aimTo.timestamp
	responseDb = await db.response.create(
		data = {
			'user': {
				'connect': {
					'user_id': response.user_id,
				}
			},
			'group_id': response.group_id,
			'ai_text': response.ai_text,
			'aim_to_mood_timestamp': aim_to_mood_timestamp,
			'lastUser': {
				'connect': {
					'user_id': response.user_id
				}
			}
		}
	)
	return responseDb

async def create_one_response(response: Response, aimTo: Mood) -> Response:
	async with Prisma() as db:
		return await create_one_response_core(db, response, aimTo)

# async def main() -> None:
# 	newResponse = Response(user_id='2234',group_id=None,ai_text='第一個回應來嘍')
# 	ans = await create_one_response(newResponse)
# 	if ans != None:
# 		glog(f' => {ans}')

# if __name__ == '__main__':
#     asyncio.run(main())